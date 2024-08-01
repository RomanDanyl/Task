from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Tag, Task


class TaskListView(generic.ListView):
    model = Task

    def get_queryset(self):
        return Task.objects.all().order_by("done", "-datetime")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "apptask/task_form.html"
    success_url = reverse_lazy("apptask:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "apptask/task_form.html"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("apptask:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ["name"]
    template_name = "apptask/tag_form.html"
    success_url = reverse_lazy("apptask:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "apptask/tag_form.html"
    success_url = reverse_lazy("apptask:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("apptask:tag-list")


def task_toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect("apptask:task-list")
