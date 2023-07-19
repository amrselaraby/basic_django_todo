from django.urls import path
from . import views

urlpatterns = [
    path("addTask/", views.addTask, name="addTask"),
    path("complete/<int:pk>/", views.complete_task, name="complete_task"),
    path("incomplete/<int:pk>/", views.incomplete_task, name="incomplete_task"),
    path("edit_task/<int:pk>/", views.edit_task, name="edit_task"),
    path("delete_task/<int:pk>/", views.delete_task, name="delete_task"),
]
