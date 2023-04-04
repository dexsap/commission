from django.contrib import admin
from .models import Employee, Productivity, Position, History, IPSUser, SummaryReport

admin.site.register(IPSUser)
admin.site.register(Employee)
admin.site.register(Productivity)
admin.site.register(Position)
admin.site.register(History)
admin.site.register(SummaryReport)
