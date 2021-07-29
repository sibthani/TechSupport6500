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
   
    # generating report by admin 
   
    path('issue_csv/', views.issue_csv, name='issue_csv'),

    #report tables
    path('issue_list/', views.issuelist, name='issue_list'),
   # path('center_report/', views.centerlist, name='center_report'),
   # path('coach_report/', views.coachlist, name='coach_report'),
   # path('cluster_report/', views.clusterlist, name='cluster_report'),
   # path('issue_cat_report/', views.issuecat, name='issue_cat_report')
   # path('staff_list/', views.stafflist, name='staff_list'),
    
    path('staff_list/', views.staff_report, name='staff_list'),
    path('issue_list/', views.issuelist, name='issue_list'),
    path('center_report/', views.centerrpt, name='center_report'),
    path('coach_report/', views.coachrpt, name='coach_report'),
    path('cluster_report/', views.clusterrpt, name='cluster_report'),
    path('issue_cat_report/', views.issuecat, name='issue_cat_report'),
    #path('staff_list/', views.stafflist, name='staff_list'),

]
