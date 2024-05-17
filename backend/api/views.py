from django.shortcuts import render
# from django.http import JsonResponse , HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

# Create your views here.
@api_view(["POST","GET"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #instance = serializer.save()
        #instance = form.save()
        # print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "not good"}, status=400)
        # print(data)
        # json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={"content-type": "application/json"})