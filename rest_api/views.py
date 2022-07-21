from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_api.models import Article
from rest_api.serializers import ArticleSerializer


class ArticleGenericView(APIView):
    def get(self, request):
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
class ArticleDetails(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        
    def get(self, request, pk):
        serializer = ArticleSerializer(self.get_object(pk))
        
        return Response(serializer.data)
    
    def put(self, request, pk):
        serializer = ArticleSerializer(self.get_object(pk), request.data)
        
        # NB: The method below will also work
            # article  = self.get_object(pk)
            # serializer = ArticleSerializer(article, request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        self.get_object(pk).delete()
        
        return Response(status.HTTP_204_NO_CONTENT)

