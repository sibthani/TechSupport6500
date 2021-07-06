from django.shortcuts import render , redirect
from .forms import IssueForm
from django.contrib import messages
#from django.http import HttpResponse


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




#def home(request):
 #   context = {
 #      'posts': posts
 #           }
 #   return render(request, 'supportapp/home.html', context)


def home(request):
   # context = {}
    if request.method == 'POST':
       form = IssueForm(request.POST)

       if form.is_valid():
          username = form.cleaned_data.get('username')
          messages.success(request, f'Tech Support Support Response form submitted {username}!')
          return redirect('supportapp-home')
    else :
         form = IssueForm()
    #if form.is_valid():
      #form.save()

    #context ['form'] = form  
  
    return render(request, 'supportapp/home.html', {'form': form })


#def home(request):
    #return HttpResponse("hi")