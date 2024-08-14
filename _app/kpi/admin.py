from django.contrib import admin
from .models import Kpi

@admin.register(Kpi)
class KpiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'startdate', 'enddate', 'savingtime', 'size')