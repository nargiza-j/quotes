from django.contrib import admin

# Register your models here.
from api_v1.models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content']
    list_display_links = ['id', 'name']
    fields = ['name', 'email', 'content', 'rate', 'status', 'created_at']
    readonly_fields = ['created_at',]


admin.site.register(Quote, QuoteAdmin)