from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from todo_list.models import Task


class TaskListView(LoginRequiredMixin, generic.ListView):
    queryset = Task.objects.prefetch_related("tags").order_by(
        "done", "-created_at"
    )


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = ("title", "content", "deadline", "tags")

    def get_success_url(self):
        return reverse("todo_list:task_list")
