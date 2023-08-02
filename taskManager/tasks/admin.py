from django.contrib import admin
from .models import Task
# Register your models here.

class CreateDate(admin.ModelAdmin):
    readonly_fields = ('createDate',)

admin.site.register(Task, CreateDate)
