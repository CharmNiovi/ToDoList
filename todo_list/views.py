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


class TaskSwitchToCompletedView(LoginRequiredMixin, generic.RedirectView):
    url = reverse_lazy("todo_list:task-list")
    
    def get(self, request, *args, **kwargs):
        Task.objects.filter(pk=self.kwargs["pk"]).update(done=True)
        return super().get(request, *args, **kwargs)


class TaskSwitchToUncompletedView(LoginRequiredMixin, generic.RedirectView):
    url = reverse_lazy("todo_list:task-list")

    def get(self, request, *args, **kwargs):
        Task.objects.filter(pk=self.kwargs["pk"]).update(done=False)
        return super().get(request, *args, **kwargs)