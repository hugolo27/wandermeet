from django.shortcuts import render
from rest_framework.views import APIView


class IndexPage(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return render(request, 'index.html')


class ChatPage(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return render(request, 'chat.html')


class LoginPage(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return render(request, 'login.html')


class ProfilePage(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return render(request, 'profile.html')


class ProfilePage1(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return render(request, 'profile1.html')


class ProfilePage2(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return render(request, 'profile2.html')


class MapPage(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return render(request, 'map.html')
