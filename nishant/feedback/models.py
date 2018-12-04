from django.db import models

class Feedback(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField (max_length=10)
    feedback=models.CharField(max_length=350)
    def __str__(self):
        feebck=self.name+","+self.email+","+self.feedback
        return feebck
