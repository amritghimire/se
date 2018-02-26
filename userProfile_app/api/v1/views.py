from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.compat import authenticate
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from ...models import UserProfile
from .serializers import UserProfileSerializer


class UserProfileListCreateAPIView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    lookup_field = 'uuid'

    # Don't use UserProfile.id!


class UserProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer
    lookup_field = 'uuid'
    # Don't use UserProfile.id


class SignUp(CreateAPIView):
    """
    It enables implements creating and saving a new user profile.
    If a profile is created this returns a 201 Created response,
    with a serialized representation of the profile as the body of the response.
    If the request data provided for creating the object was invalid, a 400 Bad Request
     response will be returned, with the error details as the body of the response.
     Sample Input 1:
        {
            "dob": "14-06-1997",
            "about": "Check",
            "address": "Pokhara",
            "gender": "M",
            "website": "http://amritghimire.com",
            "profile_picture": null,
            "email": "iamritghimire+98@gmail.com",
            "first_name": "Amrit",
            "last_name": "Ghimire",
            "username": "amrit"
        }
     Sample Response1:
        HTTP 400 Bad Request
        Allow: POST, OPTIONS
        Content-Type: application/json
        Vary: Accept

        {
            "dob": [
                "Date has wrong format. Use one of these formats instead: YYYY[-MM[-DD]]."
            ],
            "username": [
                "A user with that username already exists."
            ]
        }

     Sample Input 2:
        {
            "dob": null,
            "uuid": "b8175196-553e-4c46-8f94-7f52398d2e2b",
            "about": "Check",
            "address": "Pokhara",
            "gender": "M",
            "website": "http://amritghimire.com",
            "profile_picture": null,
            "email": "iamritghimire+98@gmail.com",
            "first_name": "Amrit",
            "last_name": "Ghimire",
            "username": "amritghi"
        }

     Sample Response 2:
        HTTP 201 Created
        Allow: POST, OPTIONS
        Content-Type: application/json
        Vary: Accept

        {
            "dob": null,
            "uuid": "b8175196-553e-4c46-8f94-7f52398d2e2b",
            "about": "Check",
            "address": "Pokhara",
            "gender": "M",
            "website": "http://amritghimire.com",
            "profile_picture": null,
            "email": "iamritghimire+98@gmail.com",
            "first_name": "Amrit",
            "last_name": "Ghimire",
            "username": "amritghi"
        }
    """
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)


class Login(APIView):
    """
    Login api
    GET request to login will return
        - user instance with 200 status code if logged in
        - error detail with 401 status code if not logged in
    POST request to login will need
        - username            //username of user
        - password            //password of user
        - csrfmiddlewaretoken //for cross site verification
        - remember_me         // checkbox to remember the user
    It will return
        - error message with status code 400 if failed to login
        - user instance with 200 status code if logged in
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        user = request.user
        auth = request.auth
        if isinstance(user, AnonymousUser):
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED)
        return Response(UserProfileSerializer(user).data)

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        remember = request.data['remember_me']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user=user)
            if not remember:
                request.session.set_expiry(0)
            return Response(UserProfileSerializer(user).data)
        else:
            error = {"error": "Please check your login info again."}
            if not UserProfile.objects.filter(username=username).exists():
                error['username'] = "The username is not registered yet.Try signing up?"
            else:
                error['password'] = "That password doesn’t match. Check CAPS lock and Try again? "
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


class Home:
    pass
