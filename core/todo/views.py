from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import render

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task
# Create your views here.
class TaskListView(ListView):

    model = Task
    ordering = '-id'
    context_object_name = 'tasks'
    paginate_by = 3  # if pagination is desired


class TaskDetailView(DetailView):
    model = Task
    context_object_name = 'task'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now() 
        return context


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'todo/task_form.html'
    model = Task
    fields = ["title"]
    success_url = reverse_lazy('task:task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy('task:task-list')
    template_name_suffix = '_form'


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")

    