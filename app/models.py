from django.db import models


class StickyNote(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField()
    created_user = models.EmailField()