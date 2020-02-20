from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import TemplateView

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
    print(filename, url)
    video = Video.objects.create(user=request.user,
                                 url=url,
                                 filename=filename)
    video.save()
    messages.success(request, 'Video uploaded successfully')
    return redirect('profile')


@login_required
def profile(request):
    video = Video.objects.filter(user=request.user)
    return render(request, 'website/profile.html', context={'video': video})


class WebsiteLoginView(TemplateView, LoginView):
    template_name = 'website/login.html'
