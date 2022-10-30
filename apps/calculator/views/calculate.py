# DRF
from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Projects
from automobile.models import Car
from calculator.serializers import CalculateSerializer





@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated))
def calculate(request):

    credit = Car.objects.filter(cridets__status=1)
    leasing = Car.objects.filter(cridets__status=2)
    serializer = CalculateSerializer({'credit': credit, 'leasing': leasing})
    return Response(serializer.data)
