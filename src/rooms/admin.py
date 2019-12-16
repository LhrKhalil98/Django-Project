from django.contrib import admin

# Register your models here.
from .models import Room ,Convenience , Photo , RoomConv , Booking

admin.site.register(Room)
admin.site.register(Convenience)
admin.site.register(Photo)
admin.site.register(RoomConv)
admin.site.register(Booking)