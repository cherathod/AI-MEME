from django.db import models

class Meme(models.Model):
    prompt = models.TextField()
    caption = models.TextField()
    image_path = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption[:50]
