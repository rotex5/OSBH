from django.contrib import admin

# Register your models here.

from .models import Forum, Discussion

admin.site.register(Discussion)


class ForumMessagesInline(admin.TabularInline):
    """
    Used to show 'existing' forum messages inline below associated forum
    """
    model = Discussion
    max_num = 0


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    """
    Administration object for Forum models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of forum comments in forum view (inlines)
    """
    list_display = ('topic', 'creator', 'date_created')
    inlines = [ForumMessagesInline]
