from django.contrib import admin
from .models import TodayFeed


class FeedAdmin(admin.ModelAdmin):
    list_display = ['title','url','date']
    list_display_links = ['title','url']

admin.site.register(TodayFeed, FeedAdmin)



