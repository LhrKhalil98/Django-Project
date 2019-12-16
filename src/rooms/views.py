from django.shortcuts import render , get_object_or_404, redirect
from .models import Room , Convenience , Photo , RoomConv 
from django.contrib.auth.decorators import login_required 
from . import forms
# Create your views here.
def room_list_view(request):
    queryset = Room.objects.all() 
    obj = Photo.objects.all()
    obj2= RoomConv.objects.all()
    context = {
        "object_list": queryset,
        "obj":obj , 
        "obj2":obj2 
    }
    return render(request, "rooms.html", context)

def room_detail_view(request, id):
    obj  = get_object_or_404(Room, id=id)
    name = obj.name
    obj2 = Photo.objects.filter(idRoom__name=name)
    obj3 = RoomConv.objects.filter(room__name=name)
    

    context = {
        "object": obj ,
        "obj":obj2,
        "name":name,
        "obj3": obj3 ,
        
    }
    return render(request, "room.html", context)

    

@login_required(login_url="/accounts/signup1/")
def booking_create(request ,id ):
    if request.method=='POST': 
        form = forms.CreateBooking(request.POST)
        if form.is_valid(): 
            instance = form.save(commit=False)
            instance.client = request.user
            obj  = get_object_or_404(Room, id=id)
            instance.room = obj ; 
            instance.save()
            return redirect('home')
    else: 
        form = forms.CreateBooking()

    return render (request,'booking.html', {'form':form})










 