from django.urls import path
from .views import CreateTaskView


urlpatterns = [
    path('create_task', CreateTaskView.as_view()),
]
