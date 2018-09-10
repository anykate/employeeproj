from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)

    STATUS = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )
    # Active/Inactive
    status = models.CharField(max_length=8, choices=STATUS, default='INACTIVE')

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
