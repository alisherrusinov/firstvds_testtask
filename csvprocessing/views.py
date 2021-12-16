from rest_framework.response import Response
from rest_framework.views import APIView
from .celery import celery_app
from celery import current_app
from time import time
from .tasks import csv_task
from .models import Task



class CreateTaskView(APIView):
    def post(self, request):
        filename = request.data.get('filename')
        task = csv_task.delay(filename=filename)
        return Response({"success": f"Task '{task.id}' created successfully"})


class AllTasks(APIView):
    def get(self, request):
        active = celery_app.control.inspect().active()
        all_tasks = []
        if active is not None:
            for node, tasks in active.items():
                all_tasks += tasks
        return Response({'Count:': len(all_tasks)})


