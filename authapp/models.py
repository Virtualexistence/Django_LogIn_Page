from django.db import models
# Create your models here.


class Context(models.Model):
    type = models.CharField(max_length=10, default="Django")

    def __str__(self):
        return self.type


class Heading(models.Model):
    title = models.CharField(max_length=50, default="Empty")
    stuff = models.TextField(null=True)

    title_txt = models.ForeignKey(Context, on_delete= models.CASCADE, null= True)
    def __str__(self):
        return self.title