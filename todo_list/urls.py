from todo_list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskSwitchToCompletedView,
    TaskSwitchToUncompletedView
)
from django.urls import path


urlpatterns = [
    path('', TaskListView.as_view(), name="task-list"),
    path('create/', TaskCreateView.as_view(), name="task-create"),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name="task-update"),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name="task-delete"),
    path('task/<int:pk>/switch_to_done', TaskSwitchToCompletedView.as_view(), name="task-switch-to-done"),
    path('task/<int:pk>/switch_to_undone', TaskSwitchToUncompletedView.as_view(), name="task-switch-to-undone"),
]

app_name = "todo_list"
