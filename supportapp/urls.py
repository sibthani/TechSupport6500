from django.urls import include, path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.index, name='index'),

    # path('home/', views.home, name='home'),

    
    path('coach/', views.coach, name='coach'),
    path('cluster/', views.cluster, name='cluster'),
    path('center/', views.center, name='center'),
    path('staff/', views.staff, name='staff'),
    path('issue_category/', views.issue_category, name='issue_category'),
    #issue page for users
    path('issue_list/', views.issuelist, name='issue_list'),
    # generating report by admin 
    path('issue_text/', views.issue_text, name='issue_text'),
    path('issue_csv/', views.issue_csv, name='issue_csv'),
    path('issue_pdf/', views.issue_pdf, name='issue_pdf'),
    #report table for admin
    path('issue-report/',views.issuesrpt, name='issue-report'),
    path('center_report/', views.centerrpt, name='center_report'),
    path('coach_report/', views.coachrpt, name='coach_report'),
    path('cluster_report/', views.clusterrpt, name='cluster_report'),
]
