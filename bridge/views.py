import os
from django.conf import settings
from django.shortcuts import render

# Create your views here.
from os.path import isfile, join


def home(request):
    directory_to_scan = os.path.join(settings.BASE_DIR, "templates", "bridge")
    onlyfiles = [f for f in os.listdir(directory_to_scan) if isfile(join(directory_to_scan, f))]
    onlyfiles.remove("base.html")
    context = {
        "files": onlyfiles
    }
    return render(request, 'bridge/base.html', context=context)


def template(request, template_name="base"):
    return render(request, 'bridge/' + template_name)
