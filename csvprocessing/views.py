from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import csv_task

class CreateTaskView(APIView):
    def post(self, request):
        filename = request.data.get('filename')
        task = csv_task.delay(filename=filename)
        return Response({"success": f"Task '{task.id}' created successfully"})

