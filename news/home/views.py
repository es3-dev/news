from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import author, section, new
import re

# Create your views here.
def index(request):
    news = new.objects.all()
    return render(request, 'home/index.html',{
        'news': news,
    })

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

def register(request):
    if request.method == 'GET':
        print('metodo GET')
        return render(request, 'accounts/register.html', {'show_header_buttons': False})
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
            return render(request, 'accounts/register.html', {'error': msg_validate, 'show_header_buttons': False})
        if User.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {'error': 'The entered email already exists with another user', 'show_header_buttons': False})
        #username=username | El primero es el parámetro de la funcion, lo que espera recibir | el segundo es el argumento que le enviamos que en este caso es la info del input
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {'error': 'The user already exists', 'show_header_buttons': False})
        user = User.objects.create_user(username, password)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        return redirect('index')




def log(request):
    return render(request, 'accounts/login.html', {'show_header_buttons': False})