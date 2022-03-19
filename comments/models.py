from django.db import models

class Comment(models.Model):
    author = models.CharField(max_length=50)
    text = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f'{self.author} {self.text}'

