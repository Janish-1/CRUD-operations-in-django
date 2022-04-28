from django.db import models

class RegisterModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)

    def __str__(self):
        return str(self.id) + ':' + self.name + ':' + self.email   #self.id is the labelling of the data and ':' is to show ?
