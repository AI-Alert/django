from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'description', 'body', 'author_id')

# class RubricsSerializer(serializers.ModelSerializer):

#     rubrics = ArticleSerializer(many=True, read_only=True)

#     class Meta:
#         model = Rubric
#         fields = (
#             "id",  # Put an Id if you want!
#             "rubrics",
#         )