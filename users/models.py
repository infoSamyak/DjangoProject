from django.db import models

# Create your models here.


class Users(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    age = models.IntegerField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'apis_users'
        ordering = ['id']

    def __str__(self):
        return f"{self.fname} {self.lname}"
