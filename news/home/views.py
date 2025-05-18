from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import author, section, new
import re
from django.views.decorators.http import require_POST

# Create your views here.

def validate_password(password):
    if len(password) < 8:
        return 'Password must contain at least 8 characters'
    if not re.search(r'[A-Z]', password):
        return 'Must include at least one uppercase letter'
    if not re.search(r'[a-z]', password):
        return 'Must include at least one lowercase letter'
    if not re.search(r'\d', password):
        return 'Must include at least one number'
    if not re.search(r'[@$!%*?&]', password):
        return 'Must include at least one special character (@, $, !, %, *, ?, &)'
    return None #Esto nos indica que la contraseña cumple todos los criterios.

def user_register(request):
    if request.method == 'GET':
        print('metodo GET')
        return render(request, 'registration/register.html')
    elif request.method == 'POST':
        print('metodo POST')
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        
        msg_validate = validate_password(password)
        if msg_validate:
            print({'error': msg_validate})
            return render(request, 'registration/register.html', {'error': msg_validate})
        if User.objects.filter(email=email).exists():
            return render(request, 'registration/register.html', {'error': 'The entered email already exists with another user'})
        #username=username | El primero es el parámetro de la funcion, lo que espera recibir | el segundo es el argumento que le enviamos que en este caso es la info del input
        if User.objects.filter(username=username).exists():
            return render(request, 'registration/register.html', {'error': 'The user already exists'})
        user = User.objects.create_user(username, password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        # Login automático tras registro
        login(request, user)
        return redirect('index')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_authenticated = authenticate(request, username=username, password=password)
        if user_authenticated is not None:
            login(request, user_authenticated)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'error': 'User does not exist'})


@require_POST
def user_logout(request):
    logout(request)
    return redirect('index')

def index(request):
    news = new.objects.all()
    latest_news = new.objects.filter(published=True).order_by('-date')[:4]
    return render(request, 'home/index.html',{
        'news': news,
        'latest_news': latest_news,
    })

def technology(request):
    technology_section = section.objects.filter(name_section__iexact='Tecnologia').first()
    technology_news = new.objects.filter(section=technology_section, published=True).order_by('-date')
    return render(request, 'technology/technology.html', {'news': technology_news})

def science(request):
    science_section = section.objects.filter(name_section__iexact='Ciencia').first()
    science_news = new.objects.filter(section=science_section, published=True).order_by('-date')
    return render(request, 'science/science.html', {'news': science_news})

def economy(request):
    economy_section = section.objects.filter(name_section__iexact='Economia').first()
    economy_news = new.objects.filter(section=economy_section, published=True).order_by('-date')
    return render(request, 'economy/economy.html', {'news': economy_news})

def entertainment(request):
    entertainment_section = section.objects.filter(name_section__iexact='Entretenimiento').first()
    entertainment_news = new.objects.filter(section=entertainment_section, published=True).order_by('-date')
    return render(request, 'entertainment/entertainment.html', {'news': entertainment_news})

def politics(request):
    politics_section = section.objects.filter(name_section__iexact='Politica').first()
    politics_news = new.objects.filter(section=politics_section, published=True).order_by('-date')
    return render(request, 'politics/politics.html', {'news': politics_news})