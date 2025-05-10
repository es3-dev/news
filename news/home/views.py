from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import autor, seccion, noticia

# Create your views here.
def index(request):
    main = noticia.objects.all()
    return render(request, 'home/index.html',{
        'noticia': noticia,
    })

def auth(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/admin/')
            else:
                return redirect('/')
        else:
            error = 'Credenciales incorrectas.'
    return render(request, 'accounts/login.html', {'error': error})
