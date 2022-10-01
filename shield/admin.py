from django.contrib import admin
from . import models

@admin.register(models.PostData)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'time',)
    search_fields = ['data__contains']
