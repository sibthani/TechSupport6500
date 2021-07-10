from django.shortcuts import render , redirect
from .forms import IssueForm
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
          # messages.success(request, f'Tech Support  Response form submitted {username}!')
          return redirect('form')
    else :
         form = IssueForm()

    context = {
        'form': form,
    }
  
    return render(request, 'supportapp/form.html', context)


def issuesrpt(request):

    context = {
        'centr_issue': Issue.objects.all(),
    }

    return render(request,'supportapp/issue-report.html', context)