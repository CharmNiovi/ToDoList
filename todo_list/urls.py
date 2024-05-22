from todo_list.views import TaskListView
from django.urls import path


urlpatterns = [
    path('', TaskListView.as_view(), name="task_list"),
]

app_name = "todo_list"
