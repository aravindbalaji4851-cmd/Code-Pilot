from django.urls import path

from exams.views import AssessmentListView,AssessmentCreateView,AssessmentRetrieveUpdateDelete


urlpatterns = [
    path('all/',AssessmentListView.as_view()),
    path('add/',AssessmentCreateView.as_view()),
    path('assessments/<int:pk>/',AssessmentRetrieveUpdateDelete.as_view()),
]