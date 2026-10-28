from django.shortcuts import render

from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from exams.models import Assessment

from problem.models import Question
from problem.serializers import QuestionSerializer
# Create your views here.


class QuestionCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def post(self,request,pk=None):

        assessment_id = pk

        assessment_obj = Assessment.objects.get(id=assessment_id)

        form_data = request.data

        serializer = QuestionSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(assessment=assessment_obj,created_by=request.user)

            return Response(data=serializer.data)

        else: return Response(data=serializer.errors)


class QuestionRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    
    permission_classes = [permissions.IsAdminUser]

    serializer_class = QuestionSerializer

    queryset = Question.objects.all()

