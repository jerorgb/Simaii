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

        # Verificar usuario y contraseña
        user = authenticate(username=usuario, password=clave)

        if user is not None:
            # Usuario registrado y contraseña correcta → redirige a home
            login(request, user)
            return redirect("Home")
        else:
            # Usuario no existe o contraseña incorrecta → se queda en login
            error = "Usuario o contraseña incorrectos"

    # Renderiza login.html con posible mensaje de error
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
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        clave = request.POST.get("clave")
        confirmar_clave = request.POST.get("confirmar_clave")

        # Validar que las contraseñas coincidan
        if clave != confirmar_clave:
            error = "Las contraseñas no coinciden"
            return render(request, "registro.html", {"error": error})

        # Verificar si el usuario ya existe
        if User.objects.filter(username=usuario).exists():
            error = "Ese usuario ya existe"
            return render(request, "registro.html", {"error": error})

        # Crear el usuario con nombre, apellido, correo y contraseña
        User.objects.create_user(
            username=usuario,
            first_name=nombre,
            last_name=apellido,
            email=email,
            password=clave
        )

        return redirect("Login")

    return render(request, "registro.html")




