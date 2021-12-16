from rest_framework.response import Response
from rest_framework.views import APIView
from .celery import celery_app
from celery import current_app
from .tasks import csv_task


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

class TaskResult(APIView):
    def post(self, request):
        task_id = request.data.get('id')
        task = current_app.AsyncResult(task_id)
        response_data = {'task_status': task.status, 'task_id': task.id}
        if task.status == 'SUCCESS':
            result = task.get()
            response_data['result'] = result
        return Response(response_data)



