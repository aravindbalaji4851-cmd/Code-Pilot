from django.urls import path

from evaluation.views import SubmissionStartView,SubmissionRetrieveView 
from evaluation.views import AnswerCreateView

urlpatterns = [
    path('assessment/<int:pk>/submission/',SubmissionStartView.as_view()),
    path('submission/<int:pk>/answer/',AnswerCreateView.as_view()),
    path('submission/<int:pk>/',SubmissionRetrieveView.as_view()),
]