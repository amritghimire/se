from django import forms

from .models import UserProfile


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = {
            'first_name',
            'last_name',
            'username',
            'email',
            'gender',
        }

    def save(self, commit=True):
        return super().save(False)
