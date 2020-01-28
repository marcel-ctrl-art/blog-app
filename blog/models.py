from django.db import models


class Post(models.Model):
    """The reference is to the built-in Django User model."""
    title = models.CharField(blank=True, max_length=256)
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

