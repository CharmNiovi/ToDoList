from django.contrib import admin
from todo_list.models import Task, Tag

admin.site.register(Tag)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Task', {
            'fields': ['content', 'deadline', 'done', 'tags']
        }),
    ]
    list_display = ('created_at', 'deadline', 'done')
    list_filter = ("done",)
    search_fields = ("tags__name",)
