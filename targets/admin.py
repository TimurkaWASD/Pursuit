from django.contrib import admin
from targets.models import Target


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date_start', 'date_end', 'status', 'favorite')
    list_filter = ('status', 'favorite', 'date_start', 'date_end')
    search_fields = ('name', 'description')
    readonly_fields = ('date_start',)
