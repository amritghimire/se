from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Category
from userProfile_app.models import UserProfile
from .forms import SelectCategoryForm


# Create your views here.
@login_required
def select_category_user_view(request):
    user = request.user  # type: UserProfile
    if request.method == "POST":
        form = SelectCategoryForm(request.POST)
        if form.is_valid():
            if user.uuid == form.cleaned_data['user']:
                categories = form.cleaned_data['category']
                disp = " "
                for category_id in categories:
                    try:
                        category = Category.objects.get(id=category_id)
                        user.selected_category.add(category)
                    except ObjectDoesNotExist:
                        return HttpResponseBadRequest()
                return HttpResponseRedirect(reverse('bridge_app:index'))
            else:
                return HttpResponseBadRequest()
        else:
            return HttpResponseBadRequest()
    form = SelectCategoryForm(initial={'user': request.user.uuid})
    categories_list = user.selected_category.all()
    return render(request, 'account/signup_select_category.html', context={'form': form, 'categories': categories_list})
