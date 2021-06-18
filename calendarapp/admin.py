from django.contrib import admin
from calendarapp.models import Event, EventMember

# Register your models here.

class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ['event', 'user']

admin.site.register(Event)
admin.site.register(EventMember, EventMemberAdmin)
