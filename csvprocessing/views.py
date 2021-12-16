from rest_framework.response import Response
from rest_framework.views import APIView


class CreateTaskView(APIView):
    def post(self, request):
        filename = request.data.get('filename')
        return Response({"success": f"Task '' created successfully"})

