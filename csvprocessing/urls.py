from django.urls import path
from .views import CreateTaskView, AllTasks, TaskResult


urlpatterns = [
    path('create_task', CreateTaskView.as_view()),
    path('all_tasks', AllTasks.as_view()),
    path('task_result', TaskResult.as_view()),
]
