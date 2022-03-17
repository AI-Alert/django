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


# class Rubric(models.Model):
#     rubric_name = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         ordering = ['id']  # Create a ordering!

#     def __str__(self):
#         return self.rubric_name


