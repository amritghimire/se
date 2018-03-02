from ajax_select import make_ajax_field
from django import forms
from .models import Category
from userProfile_app.models import UserProfile
from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField


class SelectCategoryForm(forms.Form):
    category = AutoCompleteSelectMultipleField('categories', help_text="")
    user = forms.UUIDField(widget=forms.HiddenInput())
