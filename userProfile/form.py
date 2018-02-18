from django import forms

from .models import UserProfile


class SignUpForm(forms.Form):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
        ('U', "Unspecified")
    )
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(), required=True)

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.gender = self.cleaned_data['gender']
        user.save()
