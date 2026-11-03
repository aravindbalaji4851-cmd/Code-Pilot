from django.shortcuts import render

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.serializers import UserSerializer
from accounts.serializers import StudentProfileSerializer
from accounts.models import User
from accounts.models import StudentProfile

from evaluation.permissions import IsStudentUser

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



class ProfileUpdateView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsStudentUser]

    def put(self,request):

        form_data = request.data

        # student_profile_obj = request.user.student

        student_profile_obj = StudentProfile.objects.get(student=request.user)

        serializer = StudentProfileSerializer(data=form_data,instance=student_profile_obj)

        if serializer.is_valid():

            serializer.save()

            return Response(data=serializer.data)

        else: return Response(data=serializer.errors)

    
class ProfileDetailView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsStudentUser]

    def get(self,request):

        profile_instance = StudentProfile.objects.get(student=request.user)

        serializer = StudentProfileSerializer(profile_instance)

        return Response(data=serializer.data)
    
