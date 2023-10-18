from django.db import models
import uuid

# Create your models here.

class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Compliance(Common, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True)


class Product(Common, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=True)


class Application(Common, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    compliance = models.ForeignKey('Compliance', models.CASCADE, related_name='comp_app')
    app_name = models.CharField(max_length=50, null=True)
    product = models.OneToOneField('Product', models.CASCADE, related_name='app_product')