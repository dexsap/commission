from django.contrib import admin
from .models import Employee, Productivity, Position, History, User

admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Productivity)
admin.site.register(Position)
admin.site.register(History)


