from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import UserSerializer
from accounts.models import User

class AdminCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data =serializer.validated_data

            instance = User.objects.create_superuser(role="admin",** cleaned_data)

            serial_inst  = UserSerializer(instance)

            return Response(data=serial_inst.data)

        else: return Response(data=serializer.errors)


class StudentCreateView(APIView):

    def post(self,request):

        form_data = request.data

        serializer = UserSerializer(data=form_data)

        if serializer.is_valid():

            cleaned_data = serializer.validated_data

            instance = User.objects.create_user(** cleaned_data,role="student")

            serializer_inst = UserSerializer(instance)

            return Response(data=serializer_inst.data)

        else: return Response(data=serializer.errors)



