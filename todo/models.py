from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)

    def __str__(self):
        """create a dunder method called str so __STR__ and we'll just return self.name and 
        this will return the name of the object or the name of the instance of that object 
        instead of the type which will give us a more readable friendly representation when reviewed in the admin panel.
        """
        return self.name