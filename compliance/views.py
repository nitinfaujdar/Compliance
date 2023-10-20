from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import *
from .serializers import *

# Create your views here.

class ApplicationView(GenericAPIView):
    serializer_class = ApplicationSerializer
    pagination_class = PageNumberPagination

    # Post request for adding the applications and its product simultaneously
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': "Application Added Successfully", 'data': serializer.data},
                        status=status.HTTP_200_OK)
    
    # Get API for list of applications and its product using pagination(10 objects per page for better response time)
    def get(self, request):
        queryset = Application.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return Response({'message': 'Applications retrieved Successfully', 'data': response.data}, 
                        status=status.HTTP_200_OK)


class ComplianceView(GenericAPIView):
    serializer_class = ComplianceSerializer
    pagination_class = PageNumberPagination

    def post(self, request):
        # create for creating new compliance and applications under it
        # get for updating the list of application for existing compliance
        try:
            obj = Compliance.objects.get_or_create(compliance=request.data.get('compliance'))
        except:
            raise serializers.ValidationError({'error_message': 'Invalid Input'})
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': "Compliance Added Successfully", 'data': serializer.data},
                        status=status.HTTP_200_OK)
    
    # Get request for list of compliance and apps and its product under this category
    # Using pagination in get request(10 objects per page for better response time)
    def get(self, request):
        queryset = Compliance.objects.all()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        response = self.get_paginated_response(serializer.data)
        return Response({'message': 'Compliance retrieved Successfully', 'data': response.data}, 
                        status=status.HTTP_200_OK)