from django.urls import path

from apptask.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    task_toggle_status,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>", TagDeleteView.as_view(), name="tag-delete"),
    path('tasks/toggle-status/<int:pk>/', task_toggle_status, name='task-toggle-status'),
]


app_name = "apptask"
