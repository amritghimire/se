from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseBadRequest,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Tag
from userProfile_app.models import UserProfile
from .forms import SelectTagForm


# Create your views here.
def select_tag_user_view(request):
    user = request.user  # type: UserProfile
    if request.method == "POST":
        form = SelectTagForm(request.POST)
        if form.is_valid():
            if user.uuid == form.cleaned_data['user']:
                tags = form.cleaned_data['tags']
                for tag_id in tags:
                    try:
                        tag = Tag.objects.get(id=tag_id)
                        tag.selected_by.add(user)
                    except ObjectDoesNotExist:
                        return HttpResponseBadRequest()
                return HttpResponseRedirect(reverse('bridge_app:index'))
            else:
                return HttpResponseBadRequest()
        else:
            return HttpResponseBadRequest()
    form = SelectTagForm(initial={'user': request.user.uuid})
    tags_list = user.selected_tag.all()
    return render(request, 'account/signup_select_tag.html', context={'form': form, 'tags': tags_list})
