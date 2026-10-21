from django.contrib import admin
from .models import Book, UserProfile, Person, Passport, Department, Employee


# Register your models here.
admin.site.register(Book)
admin.site.register(UserProfile)
admin.site.register(Person)
admin.site.register(Passport)
admin.site.register(Department)
admin.site.register(Employee)
