from django.contrib import admin
from .models import User, Setting

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at', 'status']

admin.site.register(Setting,SettingAdmin)
admin.site.register(User)



