from django.shortcuts import render
from rest_framework.views import APIView


class HomePage(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        return render(request, 'index.html')
