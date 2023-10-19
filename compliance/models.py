from django.db import models
import uuid

# Create your models here.

class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class Application(Common, models.Model):
    application_name = models.CharField(max_length=50, null=True)
    product_name = models.CharField(max_length=50)

class Compliance(Common, models.Model):
    compliance = models.CharField(max_length=50, null=True)
    applications = models.CharField(max_length=1500,null=True)