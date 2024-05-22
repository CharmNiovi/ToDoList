from django.db.models import F
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    queryset = Task.objects.prefetch_related("tags").order_by(
        "done", "-created_at"
    )


class TaskCreateView(generic.CreateView):
    model = Task
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("todo_list:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ("content", "deadline", "tags")
    success_url = reverse_lazy("todo_list:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_list:task-list")


class TaskSwitchView(generic.RedirectView):
    url = reverse_lazy("todo_list:task-list")
    
    def get(self, request, *args, **kwargs):
        Task.objects.filter(pk=self.kwargs["pk"]).update(done=~F('done'))
        return super().get(request, *args, **kwargs)


class TagListView(generic.ListView):
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ("name", )
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name", )
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
