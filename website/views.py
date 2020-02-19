from django.contrib.auth.views import LoginView
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
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
def profile(request):
    video = Video.objects.filter(user=request.user)
    return render(request, 'website/profile.html', context={'video': video})


class WebsiteLoginView(TemplateView, LoginView):
    template_name = 'website/login.html'
