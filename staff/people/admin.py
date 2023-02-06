from django.contrib import admin
from .models import Person


@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = ('name', 'id' )





