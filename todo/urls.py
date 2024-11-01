from django.urls import path

from todo.views import TaskListView, TagListView, TaskCreateView, \
    TaskUpdateView, TaskDeleteView, complete_task, undo_task

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update/",
         TaskUpdateView.as_view(),
         name="task-update"),
    path("task/<int:pk>/delete/",
         TaskDeleteView.as_view(),
         name="task-delete"),
    path("task/<int:task_id>/complete/",
         complete_task,
         name="task-complete"),
    path("task/<int:task_id>/undo/",
         undo_task,
         name="task-undo"),
    path("tags/", TagListView.as_view(), name="tags-list"),
]

app_name = "todo"
