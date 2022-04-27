from django.db import models
class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    def __str__(self):
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    # articles = models.ManyToManyField('articles', related_name='categories', blank=True)
    def __str__(self):
            return self.title