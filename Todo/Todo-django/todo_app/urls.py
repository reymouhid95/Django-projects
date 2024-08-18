from django.urls import path
from . import views

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("toggle/<int:pk>/", views.task_toggle, name="task_toggle"),
    path("update/<int:pk>/", views.task_update, name="task_update"),
    path("delete/<int:pk>/", views.task_delete, name="task_delete"),
]
