from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, UpdateView
import pika
from django.conf import settings

from website.amqp import AmqpPublisher
from website.forms import VideoUpdateForm
from website.models import Video


def index(request):
    return render(request, 'website/index.html')


def page(request, pagename):
    try:
        template = get_template('website/pages/' + pagename + '.html')
    except TemplateDoesNotExist:
        raise Http404

    return HttpResponse(template.render(request=request))


@login_required
def add_video(request):
    url = request.POST.get('url')
    filename = request.POST.get('filename')
    language_code = request.POST.get('language_code')
    print(filename, url)
    video = Video.objects.create(user=request.user,
                                 url=url,
                                 filename=filename)
    video.save()
    messages.success(request, 'Video uploaded successfully')
    amqp_body = {'url': url,
                 'language_code': language_code,
                 'job': 'audio-extract-and-recognize',
                 }
    headers = {'video_id': video.id}
    AmqpPublisher().publish(amqp_body, headers)
    return redirect('profile')




@login_required
def del_video(request, id):
    video = Video.objects.get(pk=id)
    video.delete()
    messages.success(request, 'Video was deleted')
    return redirect('profile')


@login_required
def profile(request):
    video = Video.objects.filter(user=request.user)
    return render(request, 'website/profile.html', context={'video': video})


class WebsiteLoginView(TemplateView, LoginView):
    template_name = 'website/login.html'


class WebsiteLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'website/logout.html'
    login_url = reverse_lazy('login')
    next_page = '/'


class VideoUpdateView(LoginRequiredMixin, UpdateView):
    model = Video
    form_class = VideoUpdateForm
    login_url = reverse_lazy('login')