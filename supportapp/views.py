from django.shortcuts import render , redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse4


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




def home(request):
    context = {
       'posts': posts
       
            }

    return render(request, 'supportapp/index.html', context)



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



def issue_category(request):
    if request.method == 'POST':
       form = Issue_CatgryForm(request.POST)
       if form.is_valid():
          new_issue_category = form.save(commit=False)
          new_issue_category.save()
          # username = form.cleaned_data.get('username')
          #messages.success(request,'Tech Support  Response form submitted !')
          return redirect('issue_category')
    else :
         form = Issue_CatgryForm()

    context = {
        'form': form,
    }    
  
    return render(request, 'supportapp/issue_category.html', context)



def issuesrpt(request):

    context = {
        'centr_issue': Issue.objects.all(),
    }

    return render(request,'supportapp/issue-report.html', context)