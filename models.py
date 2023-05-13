from django.db import models

# Create your models here.
class Coupon(models.Model):
 code = models.CharField(max_length=20, unique=True)
 points_needed = models.PositiveIntegerField()
 expiration_date = models.DateField()
 sponsor_name = models.CharField(max_length=50)

 def __str__(self):
    return self.code