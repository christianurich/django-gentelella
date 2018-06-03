from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404

from .models import Project, Employee, Resource


def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def project(request):
    context = {
        "projects": Project.objects.all()
    }
    return render(request, "app/projects.html", context)


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))

