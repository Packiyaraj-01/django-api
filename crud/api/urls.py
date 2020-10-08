from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview,name="api-overview"),
    path('task-list/',views.taskList,name="taskList"),
    path('task-detail/<str:pk>',views.taskDetailView,name="taskDetailView"),
    path('task-create/',views.taskCreate,name="taskCreate"),
    path('task-update/<str:pk>',views.taskUpdate,name="taskUpdate"),
    path('task-delete/<str:pk>',views.taskDelete,name="taskDelete")
]