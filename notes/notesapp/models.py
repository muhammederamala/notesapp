from django.db import models
from django.contrib.auth.models import User

class note_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    text = models.TextField()
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    video = models.FileField(upload_to='video/', blank=True, null=True)
    
    def __str__(self):
        return self.text
