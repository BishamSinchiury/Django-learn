from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        default='ram',
        unique=True
        )