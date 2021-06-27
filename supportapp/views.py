from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
      'author':'sibthani',
        'title':'Issue related to laptops',
        'content':'laptop failed to powerup',
        'date_posted':'july 23, 2018'
    }

]




def home(request):
    context = {
        'posts': posts
             }
    return render(request, 'supportapp/home.html', context)
    

