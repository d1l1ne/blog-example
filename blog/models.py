from django.db import models

# Create your models here.
class Post(models.Model):

    post_title = models.CharField(max_length=100)
    post_date = models.DateTimeField()
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='event_images/')

    def get_summary(self):
        if len(self.post_text)<70:
            return self.post_text
        else:
            return self.post_text[:70]+'...'

    def __str__(self):
        return self.post_title