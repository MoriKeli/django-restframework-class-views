from rest_framework import serializers
from rest_api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        exclude = ['date']