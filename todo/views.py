from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo/index.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = True
    task.save()
    return redirect("todo:index")


@login_required
def undo_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = False
    task.save()
    return redirect('todo:index')


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    context_object_name = "tag_list"
