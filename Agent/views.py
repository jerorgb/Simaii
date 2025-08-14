from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def Login(request):
    error = None
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        clave = request.POST.get("clave")
        user = authenticate(username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return redirect("Home")
        else:
            error = "Usuario o contraseña incorrectos"
    return render(request, "login.html", {"error": error})


# Página "About"
def About(request):
    return render(request, 'about.html')

# Página de inicio (Home)
def Home(request):
    return render(request, 'home.html')

# Página de registro

def registro(request):
    if request.method == "POST":
        usuario = request.POST.get("usuario")
        email = request.POST.get("email")
        clave = request.POST.get("clave")

        # Verificar si ya existe
        if User.objects.filter(username=usuario).exists():
            error = "Ese usuario ya existe"
            return render(request, "registro.html", {"error": error})

        # Crear usuario
        User.objects.create_user(username=usuario, email=email, password=clave)
        return redirect("Login")
    return render(request, "registro.html")

