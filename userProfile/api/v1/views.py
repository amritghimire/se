from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.compat import authenticate
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import (
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
            error={"error":"Please check your login info again."}
            if not UserProfile.objects.filter(username=username).exists():
                error['username']="The username is not registered yet.Try signing up?"
            else:
                error['password']="That password doesn’t match. Check CAPS lock and Try again? "
            return Response(error, status=status.HTTP_400_BAD_REQUEST)


class Home:
    pass
