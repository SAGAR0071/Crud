from django.db import models


class Position (models.Model):
    pos = models.CharField (max_length=20)

    def __str__(self):
        return self.pos


class Employee (models.Model):
    empid = models.CharField (max_length=20)
    Name = models.CharField (max_length=20)
    email = models.EmailField (max_length=40)
    Mobile = models.CharField (max_length=10)
    position = models.ForeignKey (Position, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ['-pk']
