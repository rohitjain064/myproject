from django.db import models
from django.utils import timezone

# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=50)
    comment=models.TextField()
    date_added=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name +"," + self.comment
