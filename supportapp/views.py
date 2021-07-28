from django.shortcuts import render , redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import csv

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter 

from django.db.models import Avg, Count, Min, Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def home(request):
    
    context = {
        'sys_user': CoachUser.objects.all(),
        'coach_issues': Issue.objects.all(),

      # 'posts': posts
       
            }

    return render(request, 'supportapp/index.html', context)

#users view
@login_required
def issuelist(request):
    sys_user = CoachUser.objects.filter(username="Sibthani")

    if sys_user == "Sibthani":
        i_issues = Issue.objects.all()

    else:

        i_issues = Issue.objects.filter(username_id=request.user)

    page = request.GET.get('page', 1)

    paginator = Paginator(i_issues, 5)
    try:
        issuelist = paginator.page(page)
    except PageNotAnInteger:
        issuelist = paginator.page(1)
    except EmptyPage:
        issuelist = paginator.page(paginator.num_pages)

    return render(request,'supportapp/issue_list.html', { 'issuelist' : issuelist }) 




@login_required
def index(request):
   # context = {}
    if request.method == 'POST':
       form = IssueForm(request.POST)
       if form.is_valid():
          user=form.save()
          new_issue = form.save(commit=False)
          new_issue.save()
          # username = form.cleaned_data.get('username')
          #messages.success(request, f'Tech Support  Response form submitted !')
          return redirect('index')
    else :
         form = IssueForm()

    context = {
        'issue_cat': Issue_Catgry.objects.all(),
        'user_details': CoachUser.objects.get(username=request.user.username),
        'form': form,
    }
  
    return render(request, 'supportapp/index.html', context)

#coach form
@login_required
def coach(request):
    if request.method == 'POST':
       form = CoachUserForm(request.POST)
       if form.is_valid():
          new_coach = form.save(commit=False)
          new_coach.save()
          return redirect('coach')
    else :
         form = CoachUserForm()

    context = {
        'user_lvl': Staff.objects.all(),
        'cluster': Cluster.objects.all(),
        'centre': Center.objects.all(),
        'form': form,
    }
       
  
    return render(request, 'supportapp/coach.html', context)

#cluster form
@login_required
def cluster(request):
   # context = {}
    if request.method == 'POST':
       form = ClusterForm(request.POST)
       if form.is_valid():
          new_cluster = form.save(commit=False)
          new_cluster.save()
          # username = form.cleaned_data.get('username')
          #messages.success(request, f'Tech Support  Response form submitted {username}!')
          return redirect('cluster')
    else :
         form = ClusterForm()

    context = {
        'form': form,
    }     
  
    return render(request, 'supportapp/cluster.html',context )

#add center form
@login_required
def center(request):
   # context = {}
    if request.method == 'POST':
       form = CenterForm(request.POST)
       if form.is_valid():
          new_center = form.save(commit=False)
          new_center.save()
          # username = form.cleaned_data.get('username')
          #messages.success(request, f'Tech Support  Response form submitted {username}!')
          return redirect('center')
    else :
         form = CenterForm()
    
    context = {
        'form': form,
    }

    return render(request, 'supportapp/center.html', context )

#Add staff from
@login_required
def staff(request):
   # context = {}
    if request.method == 'POST':
       form = StaffForm(request.POST)
       if form.is_valid():
          new_staff = form.save(commit=False)
          new_staff.save()
          # username = form.cleaned_data.get('username')
          #messages.success(request, f'Tech Support  Response form submitted {username}!')
          return redirect('staff')
    else :
         form = StaffForm()

    context = {
        'form': form,
    }    
  
    return render(request, 'supportapp/staff.html', context )


#issue Cateogry form
@login_required
def issue_category(request):
    if request.method == 'POST':
       form = Issue_CatgryForm(request.POST)
       if form.is_valid():
          new_issue_category = form.save(commit=False)
          new_issue_category.save()
          return redirect('issue_category')
    else :
         form = Issue_CatgryForm()

    context = {
        'form': form,
    }    
  
    return render(request, 'supportapp/issue_category.html', context)
   


#Generating reports for selected tables
#reports for issues

#def issuesrpt(request):

  #  context = {
     #   'centr_issue': Issue.objects.all(),
   # }

   # return render(request,'supportapp/issue-report.html', context)
"""
@login_required
def clusterlist(request):

    c_cluster = CoachUser.objects.all(),
    page = request.GET.get('page', 1)

    paginator = Paginator(c_cluster, 5)
    try:
        clusterlist = paginator.page(page)
    except PageNotAnInteger:
        clusterlist = paginator.page(1)
    except EmptyPage:
        clusterlist = paginator.page(paginator.num_pages)

    return render(request,'supportapp/cluster_report.html', { 'clusterlist' : clusterlist })


@login_required
def centerlist(request):

    c_center = CoachUser.objects.all(),
    page = request.GET.get('page', 1)

    paginator = Paginator(c_center, 5)
    try:
        centerlist = paginator.page(page)
    except PageNotAnInteger:
        centerlist = paginator.page(1)
    except EmptyPage:
        centerlist = paginator.page(paginator.num_pages)

    return render(request,'supportapp/center_report.html', { 'centerlist' : centerlist })

@login_required
def coachlist(request):

    c_coach = CoachUser.objects.all(),
    page = request.GET.get('page', 1)

    paginator = Paginator(c_coach, 5)
    try:
        coachlist = paginator.page(page)
    except PageNotAnInteger:
        coachlist = paginator.page(1)
    except EmptyPage:
        coachlist = paginator.page(paginator.num_pages)

    return render(request,'supportapp/coach_report.html', { 'coachlist' : coachlist })

@login_required
def stafflist(request):

    s_staff = CoachUser.objects.all(),
    page = request.GET.get('page', 1)

    paginator = Paginator(s_staff, 5)
    try:
        stafflist = paginator.page(page)
    except PageNotAnInteger:
        stafflist = paginator.page(1)
    except EmptyPage:
        stafflist = paginator.page(paginator.num_pages)

    return render(request,'supportapp/stafflist_report.html', { 'stafflist' : stafflist })

def issuecat(request):   
     
    i_cat = Issue_Catgry.objects.all(),
    page = request.GET.get('page', 1)

    paginator = Paginator(i_cat, 5)
    try:
        issuecat = paginator.page(page)
    except PageNotAnInteger:
        issuecat = paginator.page(1)
    except EmptyPage:
        issuecat = paginator.page(paginator.num_pages)

    return render(request,'supportapp/issue_cat_report.html', { 'issuecat' : issuecat }) 

"""

#reports for coachuser
@login_required
def coachrpt(request):

    context = {
        'coach': CoachUser.objects.all(),
    }

    return render(request,'supportapp/coach_report.html', context)



#reports for clusters
@login_required
def clusterrpt(request):

    context = {
        'cluster': Cluster.objects.all(),
    }

    return render(request,'supportapp/cluster_report.html', context)



#reports for centers
@login_required
def centerrpt(request):

    context = {
        'center': Center.objects.all(),
    }

    return render(request,'supportapp/center_report.html', context)  

@login_required
def issuecat(request):

    context = {
        'issucat': Issue_Catgry.objects.all(),
    }

    return render(request,'supportapp/issue_cat_report.html', context)

@login_required
def staff_report(request):

    context = {
        'staff_reprt': Staff.objects.all(),
    }

    return render(request,'supportapp/stafflist_report.html', context)



 

#Generating reports for issue using diffirent formats csv


# Generating reports using csv
@login_required
def issue_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response ['Content-Disposition'] = 'attachment; filename=issues.csv'
    
    #create a csv writer
    writer = csv.writer(response)

    #Designate the issues
    issues = Issue.objects.filter(username_id=request.user)

    #add columns to csv file
    writer.writerow(['Issue ID,', 'Issue_code', 'username', 'Cluster Code','Center Code','Issue Description', 'Urgenancy', ' Date Posted'])
  #loop thro and output
    for issue in issues:
       writer.writerow([issue.issue_id, issue.issue_code , issue.username , issue.cluster_code , issue.center_code , issue.issue_description , issue.urgent , issue.issue_date])


    return response

