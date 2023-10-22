from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.users.forms import UserSignin, UserSignup, UserUpdate
from django.core.exceptions import ValidationError
from apps.users.models import CustomUser
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError




def signup(request):
	if request.method == "GET":
		return render(request, "login/signup.html")
	else:	
		form = UserSignup(request.POST)
		if form.is_valid():
			user = form.save(commit= True)
			login(request, user)
			messages.success(request, "Registrado correctamente.")
			return redirect("main:home")
		else:
			for key, error in list(form.errors.items()):
				if key == "username":
					messages.error(request, "Nombre de usuario no disponible")
					continue
				elif key == "email" and error[0] == "Ya existe Custom user con este Email.":
					messages.error(request, "Inicia sessión, ya existe una cuenta con este email")
					continue
				elif key == "password2" and error[0] == "La contraseña es demasiado similar a la de username.":
					messages.error(request, "La constraseña no debe ser similar al nombre de usuario")
					continue
				elif key == "password2" and error[0] == "Los dos campos de contraseña no coinciden.":
					messages.error(request, "Contraseñas no coinciden")
					continue
				elif key == "password2":
					messages.error(request, error)
					continue
				elif key == "__all__":
					messages.error(request, error)
					continue
			return render(request, "login/signup.html")

def signin(request):
	if request.method == "GET":
		form = UserSignin()
		context = {"form": form}
		return render(request, "login/signin.html", context)
	else:
		form = UserSignin(request, request.POST)
		if form.is_valid():
			user = authenticate(
					request,
					username = request.POST["username"],
					password = request.POST["password"],
			)
			if user is not None:
				login(request, user)
				messages.success(request, f"¡Bienvenido!")
				return redirect("main:home")
		else:
			for key, error in list(form.errors.items()):
				if key == "captcha" and error[0] == "Este campo es obligatorio.":
					messages.error(
						request,
						"Debes pasar la prueba recaptcha.Intentalo de nuevo"
					)
					continue
				elif key == "__all__":
					messages.error(
						request, 
						"Porfavor, verifica que el email  y la clave sean correctos"
					)
					continue
				messages.error(request, error)
			return render(request, "login/signin.html")

def signout(request):
    logout(request)  
    return redirect("users:signin")

def signup_redirect(request):
	return redirect("main:home")

def profile(request, username):
	if request.method == "POST":
		user = request.user
		form = UserUpdate(request.POST, request.FILES, instance = user)
		if form.is_valid():
			user_form = form.save(commit= True)
			messages.success(request, "Has actualizado tu perfil")
			return redirect("users:profile", user_form.username)
	
	user = request.user
	if user:
		form = UserUpdate(instance = user)
		return render(request, "login/profile.html", {"form": form})
	
	return redirect("main:home")

def profile_delete(request, profile):
	user = get_user_model().objects.get(email = profile)
	user.delete()
	messages.success(request, "Has eliminado tu cuenta")
	return redirect("users:signin")