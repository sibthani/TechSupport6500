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

posts = [
    {
      'author':'sibthani',
        'title':'Issue related to laptops',
        'content':'laptop failed to powerup',
        'date_posted':'july 23, 2018'
    },
    {
      'author':'Bertha',
        'title':'iplay8 pro Tablet issue',
        'content':'Tablet is failing to charge',
        'date_posted':'july 23, 2018'
    }


]

@login_required
def home(request):
    
    context = {
        'sys_user': CoachUser.objects.all(),
        'coach_issues': Issue.objects.all(),
      # 'posts': posts
       
            }

    return render(request, 'supportapp/index.html', context)

#users view

def issue_list(request):
    
    context = {
        'issue_list': Issue.objects.all(),
               }

    return render(request,'supportapp/issue_list.html', context) 


def add_issue(request):
    
    context = {
        'add_issue': Issue.objects.all(),
               }

    return render(request,'supportapp/add_issue.html', context) 


#forms for all the models
#form for issues
#@login_required
def form(request):
   # context = {}
    if request.method == 'POST':
       form = IssueForm(request.POST)
       if form.is_valid():
          new_issue = form.save(commit=False)
          new_issue.save()
          # username = form.cleaned_data.get('username')
          #messages.success(request, f'Tech Support  Response form submitted !')
          return redirect('form')
    else :
         form = IssueForm()

    context = {
        'form': form,
    }
  
    return render(request, 'supportapp/form.html', context)

#coach form

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
        'form': form,
    }
       
  
    return render(request, 'supportapp/coach.html', context)

#cluster form
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

def issuesrpt(request):

    context = {
        'centr_issue': Issue.objects.all(),
    }

    return render(request,'supportapp/issue-report.html', context)

#reports for coachuser

def coachrpt(request):

    context = {
        'coach': CoachUser.objects.all(),
    }

    return render(request,'supportapp/coach_report.html', context)



#reports for clusters
def clusterrpt(request):

    context = {
        'cluster': Cluster.objects.all(),
    }

    return render(request,'supportapp/cluster_report.html', context)



#reports for centers
def centerrpt(request):

    context = {
        'center': Center.objects.all(),
    }

    return render(request,'supportapp/center_report.html', context)    
         

#Generating reports for issue using diffirent formats csv, text and pdf

#Generate pdf file for issues
def issue_pdf(request):
    #Create a byte stream buffer
    buf = io.BytesIO()
    #Create canvas
    c = canvas.Canvas(buf, pagesize=letter , bottomup=0)
    #Create text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

#Designate the issues
    issues = Issue.objects.all()

    #create blank list
    lines = []  


#create loop 
    for issue in issues: 
        lines.append(issue.issue_id)
        lines.append(issue.issue_code)
        lines.append(issue.username)
        lines.append(issue.cluster_code)
        lines.append(issue.center_code)
        lines.append(issue.issue_description)
        lines.append(issue.urgent) 
        lines.append(issue.issue_date) 
        lines.append("==========================")


    for line in lines: 
       textob.textLine(line)
    


    #finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment = True , filename='issue.pdf')


# Generating reports using csv
def issue_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response ['Content-Disposition'] = 'attachment; filename=issues.csv'
    
    #create a csv writer
    writer = csv.writer(response)

    #Designate the issues
    issues = Issue.objects.all()

    #add columns to csv file
    writer.writerow(['Issue ID,', 'Issue_code', 'username', 'Cluster Code','Center Code','Issue Description', 'Urgenancy', ' Date Posted'])
  #loop thro and output
    for issue in issues:
       writer.writerow([issue.issue_id, issue.issue_code , issue.username , issue.cluster_code , issue.center_code , issue.issue_description , issue.urgent , issue.issue_date])


    return response



def issue_text(request):
    response = HttpResponse(content_type ='text/plain')
    response ['Content-Disposition'] = 'attachment; filename=issues.txt'
    
    #create blank list
    lines = []  

    #Designate the issues
    issues = Issue.objects.all()
  #loop thro and output
    for issue in issues:
       lines.append(f'{issue.issue_id}\n {issue.issue_code}\n{issue.username}\n{issue.cluster_code}\n{issue.center_code}{issue.issue_description}\n{issue.urgent}\n{issue.issue_date}\n\n\n')

    #write to file
    response.writelines(lines)
    return response


#Generate text Files of issue List

def issue_text(request):
    response = HttpResponse(content_type ='text/plain')
    response ['Content-Disposition'] = 'attachment; filename=issues.txt'
    
    #create blank list
    lines = []  

    #Designate the issues
    issues = Issue.objects.all()
  #loop thro and output
    for issue in issues:
       lines.append(f'{issue.issue_id}\n {issue.issue_code}\n{issue.username}\n{issue.cluster_code}\n{issue.center_code}{issue.issue_description}\n{issue.urgent}\n{issue.issue_date}\n\n\n')


    #write to file
    response.writelines(lines)
    return response


