from django.shortcuts import render , redirect
#from django.contrib.auth.decorators.csrf import csrf_exempt
#from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


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
    return render(request, 'supportapp/home.html', context)


#def home(request):
  #return HttpResponse(" HI  ")