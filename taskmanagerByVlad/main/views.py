from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.generic import DetailView,UpdateView, DeleteView


class TaskDetailView(DetailView):
    model = Task
    template_name = 'main/details_view.html'
    context_object_name = 'task'


class TaskEdit(UpdateView):
    model = Task
    template_name = 'main/edit.html'

    form_class = TaskForm


class TaskDelete(DeleteView):
    model = Task
    success_url = '/'
    template_name = 'main/task-delete.html'


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Your Tasks', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Main Page')
        else:
            error = 'Form is incorrect'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


