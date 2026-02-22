from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),  # Homepage = Job list
    path('jobs/', views.job_list, name='job_list'),

    path('register/', views.register, name='register'),
    path('add/', views.add_job, name='add_job'),
    path('job/<int:pk>/', views.job_detail, name='job_detail'),

    path('verify-otp/', views.verify_otp, name='verify_otp'),
]