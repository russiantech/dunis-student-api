from django.db import models
from django.utils.timezone import now
class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)

    # created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(auto_now_add=True, default=now)
    created_at = models.DateTimeField(default=now)
    # created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title