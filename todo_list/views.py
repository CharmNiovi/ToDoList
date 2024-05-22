from django.urls import reverse_lazy
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
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = ("title", "content", "deadline", "tags")
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")
