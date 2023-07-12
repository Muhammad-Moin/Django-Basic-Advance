from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def Home(request):
    count = User.objects.count()
    return render(request,'home.html',{
        'count':count
    })

def Signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request,'registration/signup.html',{
        'form':form
    })

def Login(request):
    return render(request,'registration/login.html')