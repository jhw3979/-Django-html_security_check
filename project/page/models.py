from django.db import models

# Create your models here.

class User(models.Model):
    User_id = models.CharField(default='', max_length=50)
    User_pw = models.CharField(max_length=100)
    User_name = models.CharField(max_length=25)

    def __str__(self):
        return self.User_name


class Html_file(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField()
    upload_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

