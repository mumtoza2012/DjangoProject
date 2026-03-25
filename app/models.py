from django.db import models


class Contact(models.Model):
    name = models.CharField()
    phone_number = models.CharField()
    description = models.TextField(null=True, blank=True)


class Portfolio(models.Model):
    image = models.ImageField()
    title = models.CharField()
    user_image = models.ImageField(null=True, blank=True)
    fullname = models.CharField()

    def __str__(self):
        return self.title

