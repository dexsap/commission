from django.contrib import admin
from .models import Employee, Productivity, JobOrder, Position, History, Dashboard

admin.site.register(Employee)
admin.site.register(Productivity)
admin.site.register(JobOrder)
admin.site.register(Position)
admin.site.register(History)
admin.site.register(Dashboard)


