from todo_list.views import TaskListView, TaskCreateView
from django.urls import path


urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
    path('create_new_task', TaskCreateView.as_view(), name="task_create"),
]

app_name = "todo_list"
