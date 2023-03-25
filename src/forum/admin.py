from django.contrib import admin
from .models import Thread, Discussion
# Register your models here.

admin.site.register(Discussion)

class ThreadMessagesInline(admin.TabularInline):
    """
    Used to show 'existing' thread messages inline below associated forum
    """
    model = Discussion
    max_num = 0


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    """
    Administration object for Thread models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of thread comments in forum view (inlines)
    """
    list_display = ('title', 'author', 'timestamp')
    inlines = [ThreadMessagesInline]
