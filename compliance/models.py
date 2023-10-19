from django.db import models
import uuid

# Create your models here.

# created_at an dupdated_at field for the time management purpose(Common for all models)
class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Application(Common, models.Model):
    application_name = models.CharField(max_length=50, null=True)
    product_name = models.CharField(max_length=50)

# Here applications field will take comma separated application ids as its value
class Compliance(Common, models.Model):
    compliance = models.CharField(max_length=50, null=True)
    applications = models.CharField(max_length=1500,null=True)