from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm
from django.db.models import Q
from django.urls import reverse_lazy, reverse
# Create your views here.
class TodosList(ListView):
    model = Todo
    template_name = "todos/todo_list.html"
    context_object_name = "todos"


class SearchResultsView(ListView):
    model = Todo
    template_name = "todos/search_results.html" # Alohida HTML
    context_object_name = "results"

    def get_queryset(self):
        word = self.request.GET.get("q")
        if word:
            return Todo.objects.filter(
                Q(title__icontains=word) | Q(description__icontains=word)
            )
        return Todo.objects.none()


class CreateTodo(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = "todos/create_todo.html"
    success_url = reverse_lazy("todo_list")

class TodoDetail(DetailView):
    model = Todo
    template_name = "todos/todo_detail.html"
    context_object_name = "todo"


class UpdateTodo(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "todos/update_todo.html"
    
    def get_success_url(self):
        # Yangilangan obyektning pk raqamini olib, detail sahifasiga yuboradi
        return reverse("todo_detail", kwargs={'pk': self.object.pk})
    
class DeleteTodo(DeleteView):
    model = Todo
    template_name = "todos/delete_todo.html"
    context_object_name = "todo"
    success_url = reverse_lazy("todo_list")