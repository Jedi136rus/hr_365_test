from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def convert_value(request):
    return Response({'result': 'OK'}, status=status.HTTP_200_OK)
