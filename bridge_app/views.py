import os
from django.conf import settings
from django.shortcuts import render
from os.path import isfile, join
from relationship_app.models import Relationship


def index(request):
    if request.user.is_authenticated:
        recommended_objects = [a.product for a in
                               Relationship.objects.filter(author=request.user).order_by('-score')[:5]]
    else:
        recommended_objects = [a.product for a in Relationship.objects.all()[:5]]

    context = {
        'recommended_objects': recommended_objects
    }

    return render(request, 'bridge_app/index.html', context=context)


def home(request):
    directory_to_scan = os.path.join(settings.BASE_DIR, "templates", "bridge_app")
    onlyfiles = [f for f in os.listdir(directory_to_scan) if isfile(join(directory_to_scan, f))]
    onlyfiles.remove("home.html")
    context = {
        "files": onlyfiles
    }
    return render(request, 'bridge_app/home.html', context=context)


def template(request, template_name="base"):
    return render(request, 'bridge_app/' + template_name)
