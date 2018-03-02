from ajax_select import make_ajax_field
from django import forms
from .models import Tag
from userProfile_app.models import UserProfile
from ajax_select.fields import AutoCompleteSelectField, AutoCompleteSelectMultipleField


class SelectTagForm(forms.Form):
    tags = AutoCompleteSelectMultipleField('tags', help_text="")
    user = forms.UUIDField(widget=forms.HiddenInput())
