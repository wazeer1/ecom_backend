from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import Group, User
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from main.encryptions import *
from rest_framework import status
from .serializers import *
from api.v1.main.functions import *
from products.models import *
from main.models import *
import json



@api_view(["GET"])
@permission_classes((AllowAny,))
def offered_products(request):
    if Product.objects.filter(offer__gte = 20, is_deleted = False).exists():
        instances = Product.objects.filter(offer__gte = 20, is_deleted = False)
        serialized = ProductsSerializer(
            instances,
            context = {
            "request":request
            },
            many = True
        ).data
        response_data = {
            "StatusCode":6000,
            "data":serialized
        }
    else:
        response_data={
            "StatusCode":6001,
            "data":{
            "title":"failed",
            "message":"no offered products"
            }
        }
    return Response(response_data, status=status.HTTP_200_OK)