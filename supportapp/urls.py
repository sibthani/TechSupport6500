from django.urls import path
from. import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('form/', views.form, name='form'),
    path('issue-report/',views.issuesrpt, name='issue-report'),
    path('coach/', views.coach, name='coach'),
    path('cluster/', views.cluster, name='cluster'),
    path('center/', views.center, name='center'),
    path('staff/', views.staff, name='staff'),
    path('issue_category/', views.issue_category, name='issue_category'),
]