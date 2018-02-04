from rest_framework import serializers

from ...models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['dob','uuid','about','address','gender',
                  'website','profile_picture','email',
                  'first_name','last_name','username'
                  ]
