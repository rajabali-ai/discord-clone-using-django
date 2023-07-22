from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.
# rooms = [
#     {'id' : 1, 'name':'Lets Learn Python!'},
#     {'id' : 2, 'name':'Lets Learn Java!'},
#     {'id' : 3, 'name':'Lets Learn ML!'},
# ]



def home(request):
    rooms = Room.objects.all() 
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request,pk):
    # room=None
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i
    # context = {'room':room}

    room = Room.objects.get(id=pk)
    context = {'room': room}

    return render(request, 'base/room.html', context)

def createRoom(request):

    context={}
    return render(request, 'base/room_form.html', context)
