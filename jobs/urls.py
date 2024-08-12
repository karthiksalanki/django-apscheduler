from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.jobs, name='job-list'),
    path('jobs/<int:pk>/', views.job_detail, name='job-detail'),
    path('job/', views.createJobs, name='job-create'),

]
