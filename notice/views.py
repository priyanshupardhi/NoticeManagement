from .serializer import *
from .models import *
from rest_framework import generics, status
from rest_framework.response import Response
from .Custompagination import CustomPagination
from rest_framework import filters

# Create your views here.


"""
NoticeView api
api_endpoint = http://127.0.0.1:8000/api/notice/<int:pk>/
Method = GET, PUT, PATCH, DELETE,
DESC = using pk, list down all details, edit and delete a particular notice
get -> dictionary
post -> title, content, image, created_date
"""

class NoticeView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = NoticeSerializer
    lookup_field = 'pk'
    queryset = Notice.objects.all()
    
    def get_queryset(self):
        return super().get_queryset()

"""
NoticeListView api
api_endpoint = http://127.0.0.1:8000/api/notice-list
Method = GET, POST
DESC = list down all notices and create new notice
get -> list []
post -> title, content, image, created_date
pagination -> api//notice-list?page=<int>
search -> api//notice-list?search=<string>
order -> /api/notice-list?ordering=-created_date
"""

class NoticeListView(generics.ListCreateAPIView):
    
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    
    search_fields = ['title']
    ordering_fields = ['created_date']
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': 'Notice created.'}, status=status.HTTP_201_CREATED)
    