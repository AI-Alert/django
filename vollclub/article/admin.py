from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Article, Author, Comment, Category
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Category)