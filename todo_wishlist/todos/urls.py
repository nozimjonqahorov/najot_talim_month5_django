from django.urls import path
from .views import TodosList, CreateTodo, TodoDetail, UpdateTodo, DeleteTodo, SearchResultsView

urlpatterns = [
    path("", TodosList.as_view(), name="todo_list"),
    path("create-todo", CreateTodo.as_view(), name="create_todo"),
    path("todo-detail/<int:pk>/", TodoDetail.as_view(), name="todo_detail"),
    path("update-todo/<int:pk>/", UpdateTodo.as_view(), name="update_todo"),
    path("delete-todo/<int:pk>/", DeleteTodo.as_view(), name="delete_todo"),
    path('search/', SearchResultsView.as_view(), name='search_info'),
]
