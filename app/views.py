from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test,login_required
from app.forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Idea

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required(login_url='Userlogin')
def Userlogout(request):
    logout(request)
    return redirect('home')

@login_required(login_url='Userlogin')
def invest(request):
    Ideas = Idea.objects.all()
    return render(request,'invest.html',{'Ideas': Ideas})

def invest_idea(request , Idea_id):
    Ideas = Idea.objects.get(id= Idea_id)
    return render(request, 'invest_idea.html', {'Ideas':Ideas})

@login_required(login_url='Userlogin')
def ideas(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        instant_investment = request.POST.get('instant investment')
        total_investment = request.POST.get('total investment')
        Ideas = Idea(idea_title= title, idea_description=description, idea_instant_investment= instant_investment, idea_total_investment= total_investment)
        Ideas.save()
        messages.success(request,'Idea posted successfully and is open to investors.')
        return redirect(home)
    return render(request,'ideas.html')

def Userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:  
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Incorrect Username or Password')
            return render(request, 'login.html')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')  # You can replace 'login' with the name of your login view
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form}) 