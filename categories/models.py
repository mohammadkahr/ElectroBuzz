from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')
    description = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='categories/statics/img', blank=True, null=True)

    def __str__(self):
        return self.name
