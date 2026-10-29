from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework import serializers

from evaluation.models import Submission
from evaluation.serializers import SubmissionSerializer,AnswerSerializer
from evaluation.permissions import IsStudentUser

from exams.models import Assessment

from problem.models import Question

class SubmissionStartView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsStudentUser]

    def post(self,request,pk=None):

        assessment_id = pk

        assessment_obj = get_object_or_404(Assessment,id=assessment_id)

        instance = Submission.objects.create(student=request.user,assessment=assessment_obj)

        serializer = SubmissionSerializer(instance)

        return Response(serializer.data)


class SubmissionRetrieveView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,request,pk=None):

        instance = get_object_or_404(Submission,id=pk)

        serializer = SubmissionSerializer(instance)

        return Response(data=serializer.data)


class AnswerCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsStudentUser]

    def post(self,request,pk=None):

        submission_id = pk

        submission_obj = get_object_or_404(Submission,id=pk)

        form_data = request.data

        # validation start

        assessment_obj = submission_obj.assessment

        assessment_questions = Question.objects.filter(assessment=assessment_obj).values_list("id",flat=True)

        question = form_data.get("question")

        if question not in assessment_questions: raise serializers.ValidationError("invalid question,Question noy exist in assessment")

        # validation ends

        serializer = AnswerSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(submission=submission_obj)

            return Response(data=serializer.data)

        else: return Response(data=serializer.errors)

        