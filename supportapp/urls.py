from django.urls import path
from. import views

urlpatterns = [
    #home page
    path('home/', views.home, name='home'),
    #issue , coach, cluster, staff, center, issue_category forms
    path('form/', views.form, name='form'),
    path('coach/', views.coach, name='coach'),
    path('cluster/', views.cluster, name='cluster'),
    path('center/', views.center, name='center'),
    path('staff/', views.staff, name='staff'),
    path('issue_category/', views.issue_category, name='issue_category'),
    #issue page for users
    path('issue_list/', views.issue_list, name='issue_list'),
    path('add_issue/', views.add_issue, name='add_issue'),
    # generating report by admin 
    path('issue_text/', views.issue_text, name='issue-text'),
    path('issue_csv/', views.issue_csv, name='issue_csv'),
    path('issue_pdf/', views.issue_pdf, name='issue_pdf'),
    #report table for admin
    path('issue-report/',views.issuesrpt, name='issue-report'),
    path('center_report/', views.centerrpt, name='center_report'),
    path('coach_report/', views.coachrpt, name='cluster_report'),
    path('cluster_report/', views.clusterrpt, name='coach_report'),
]
