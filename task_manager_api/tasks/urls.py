from django.urls import path
from . import views

urlpatterns= [
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/create/', views.task_create, name='task-create'),
    path('tasks/<int:pk>/', views.task_detail , name= 'task-detail'),
    path('tasks/<int:pk>/update/', views.task_update, name= 'task-update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name= 'task-delete'),
]