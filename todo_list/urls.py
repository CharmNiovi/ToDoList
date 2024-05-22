from todo_list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)
from django.urls import path


urlpatterns = [
    path('', TaskListView.as_view(), name="task-list"),
    path('create/', TaskCreateView.as_view(), name="task-create"),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name="task-update"),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "todo_list"
