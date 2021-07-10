from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('issue-report/',views.issuesrpt, name='issue-report'),
]