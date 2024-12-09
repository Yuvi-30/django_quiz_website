from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from  django.contrib import auth
from .models import Rules
# Create your views here.


def register_now(request):
    return render(request,'register_now.html')

def index(request):
    rules = Rules.objects.all()
    return render(request,'index.html', {'rules':rules})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exist')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')  
        else:
            messages.error(request, 'passwords doesnt match')
            return redirect('register')
    else: 
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')




def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request,abc):
    return render(request,'post.html',{'abc':abc})

def example_links(request):
    posts = [1,23,4,5,6,'er','home','hello']
    return render(request, 'example_link.html',{'posts':posts})










        # rule1 = Rules()
        # rule1.details = 'Click on Next button to go to next question.'
        # rule2 = Rules()
        # rule2.details = 'Click on Prev button to go to prev question.'
        # rule3 = Rules()
        # rule3.details = 'Click on Exit button to go on home page.'
        # rule4 = Rules()
        # rule4.details = 'There are a total of 5 questions.'
        # rule5 = Rules()
        # rule5.details = 'Options once selected cannot be changed.'
        

        #rules = [rule1, rule2, rule3, rule4, rule5]