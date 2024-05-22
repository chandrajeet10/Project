from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializers

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ValidationError as e:
            # Handle validation errors
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle other exceptions
            return Response(data={'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def get_object(self):
        try:
            return super().get_object()
        except NotFound:
            raise NotFound(detail="Employee not found", code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            raise e

    def put(self, request, *args, **kwargs):
        try:
            return super().put(request, *args, **kwargs)
        except ValidationError as e:
            # Handle validation errors
            return Response(data={'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except NotFound:
            raise NotFound(detail="Employee not found", code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle other exceptions
            return Response(data={'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, *args, **kwargs):
        try:
            return super().delete(request, *args, **kwargs)
        except NotFound:
            raise NotFound(detail="Employee not found", code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Handle other exceptions
            return Response(data={'error': 'Internal Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        



