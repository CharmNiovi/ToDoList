from todo_list.views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskSwitchToCompletedView,
    TaskSwitchToUncompletedView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView
)
from django.urls import path


urlpatterns = [
    path('', TaskListView.as_view(), name="task-list"),
    path('create/', TaskCreateView.as_view(), name="task-create"),
    path('task/<int:pk>/update/',
         TaskUpdateView.as_view(),
         name="task-update"),
    path('task/<int:pk>/delete/',
         TaskDeleteView.as_view(),
         name="task-delete"),
    path('task/<int:pk>/switch_to_done/',
         TaskSwitchToCompletedView.as_view(),
         name="task-switch-to-done"),
    path('task/<int:pk>/switch_to_undone/',
         TaskSwitchToUncompletedView.as_view(),
         name="task-switch-to-undone"),

    path('tags/', TagListView.as_view(), name="tag-list"),
    path('tags/create/', TagCreateView.as_view(), name="tag-create"),
    path('tags/<int:pk>/update/', TagUpdateView.as_view(), name="tag-update"),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo_list"
