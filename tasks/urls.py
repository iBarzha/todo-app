from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:task_id>/update/', views.task_update, name='task_update'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('update_task_status/<int:task_id>/', views.update_task_status, name='update_task_status'),
]