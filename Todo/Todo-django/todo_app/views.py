from django.shortcuts import get_object_or_404, redirect, render

from .forms import TaskForm
from .models import Task


# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by("-created_at")
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    return render(request, "todo_app/task_list.html", {"tasks": tasks, "form": form})


def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "todo_app/task_update.html", {"form": form, "task": task})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("task_list")
