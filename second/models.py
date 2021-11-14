from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) #게시글이 생성될 때 자동으로 값이 만들어짐.
    updated_at = models.DateTimeField(auto_now=True)

    # num_starts =models.IntegerField()
