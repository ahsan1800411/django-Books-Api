
from .models import Book
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from rest_framework.views import APIView

# @api_view(['GET'])
# def books_list(request):
#     books=Book.objects.all();
#     serializer=BookSerializer(books,many=True);
#     return Response(serializer.data)


# @api_view(['POST'])
# def create_book(request):api_view
    
#     serializer=BookSerializer(data=request.data);
#     if serializer.is_valid():
#       serializer.save();
#       return Response(serializer.data,status=201)
    
#     return Response(serializer.errors,status=400)
    

# @api_view(['GET','PATCH',"DELETE"])
# def book(request,title):
#     book=Book.objects.get(title=title)
#     if request.method == 'GET':
#         serializer=BookSerializer(book);
#         return Response(serializer.data)
    
    
#     if request.method == 'PATCH':
#       serializer=BookSerializer(book,data=request.data);
#       if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=200)
#       return Response(serializer.errors,status=400)
    
     
#     if request.method == 'DELETE':
#         book.delete()
#         return Response("Delete book",status=204)
    
    
# class BookList(APIView):
#      def get(self,request):
#           books=Book.objects.all();
#           serializer=BookSerializer(books,many=True);
#           return Response(serializer.data)
          


class BookViewSet(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer