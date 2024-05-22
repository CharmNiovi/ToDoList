from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from todo_list.models import Task


class TaskListView(LoginRequiredMixin, generic.ListView):
    queryset = Task.objects.prefetch_related("tags").order_by(
        "done", "-created_at"
    )
