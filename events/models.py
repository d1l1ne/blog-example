from django.db import models

# Create your models here.
class Event(models.Model): #наследуем класс от model.Model
    event_image = models.ImageField(upload_to='event_images/') #создаем свойство модели
    event_text = models.CharField(max_length=300)

    def __str__(self):
        return self.event_text