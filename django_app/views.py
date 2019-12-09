from rest_framework.decorators import api_view
from datetime import datetime

from rest_framework.response import Response
from rest_framework import status as rest_status


@api_view(['GET'])
def status(request):
    date = datetime.now().strftime(" %d/%m/%Y %H:%M:%S")
    message = 'server is live at' + date
    return Response(data=message, status=rest_status.HTTP_200_OK)
