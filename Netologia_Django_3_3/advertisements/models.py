from django.db import models
from django.contrib.auth.models import User


class Advertisement(models.Model):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    DRAFT = 'DRAFT'

    STATUS_CHOICES = [
        (OPEN, 'Open'),
        (CLOSED, 'Closed'),
        (DRAFT, 'Draft'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=OPEN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='advertisements', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
