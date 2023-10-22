# Django
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from googleapiclient.discovery import build

from apps.main.models import Conocimiento
from django.contrib.auth import get_user_model

@login_required
def home(request):
    obj = Conocimiento.objects.first_conocimiento()

    context = {
        "obj": obj
    }
    return render(
        request,
        "dashboard/dashboard.html",
        context
    )

def conocimiento(request):
    videos = []
    buscar = [ "gMMmEfEJIqw"]
    for busca in range(len(buscar)):
        video = {
            'thumbnails': 420,
            'video_id': buscar[busca],
        }
        videos.append(video)

    context = {
        'videos': videos,
    }
    return render(request, "dashboard/conocimiento.html", context)

def conocimiento_read(request):
    user = get_user_model().objects.get(email = request.user.email )
    obj = Conocimiento.objects.filter(author = user)
    context = {
        "obj": obj
    }
    
    return render(request, "dashboard/conocimiento_read.html", context)


def conocimiento_create(request, video_id):
    if request.method == "POST":
        user = request.user
        user_aprende = Conocimiento.objects.create(
        conocimiento = request.POST["conocimiento"],
        author = user,
        link_video = video_id
        )
        user_aprende.save()
        return redirect("main:home")

def  conocimiento_update(request, conocimiento):
    update = Conocimiento.objects.get(id = conocimiento)
    if request.method == "POST":
        update.conocimiento = request.POST["conocimiento"]
        update.save()
        messages.success(request, "Haz actualizado tu conocimiento")
        return redirect("main:conocimiento")
    
    context = {
        "object": update
    }
    return render(request, "dashboard/conocimiento_update.html", context)


def  conocimiento_delete(request, conocimiento):
    conocimiento = Conocimiento.objects.get(id = conocimiento)
    conocimiento.delete()
    messages.success(request, "Tu conocimiento se ha eliminado")
    return redirect("main:conocimiento")

