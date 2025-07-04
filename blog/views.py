from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import re
from django.contrib import messages
from django.contrib.auth.models import User, auth
from blog.models import*
# Create your views here.

posts = [
    {
        'title': 'Beautiful is better than ugly',
        'author': 'John Doe',
        'content': 'Beautiful is better than ugly',
        'published_at': 'October 1, 2022'
    },
    {
        'title': 'Explicit is better than implicit',
        'author': 'Jane Doe',
        'content': 'Explicit is better than implicit',
        'published_at': 'October 1, 2022'
    }
]
context = {
        'posts': posts,
        'title': 'Zen of Python'
    }
def start(request):
    movies=Movie.objects.all()
    featured_movie= movies.last()
    context = {
        'movies': movies,
        'featured_movie': featured_movie,
    }
    return render(request, 'index.html', context)



def user_regirster(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info("Email is taken")
                return redirect('user_regirster')
            elif User.objects.filter(username=username).exists():
                messages.info("username is taken")
                return redirect('user_regirster')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()

                user_login=auth.authenticate(username-username,password=password)
                auth.login(request,user_login)
                return redirect('user_regirster')
        else:
            messages.info("Password is not matching..")
    else:
        return render(request,'signup.html')




