from django.db import models
import uuid


# Create your models here.
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    origin = models.TextField(max_length=16)
    sku = models.TextField(max_length=16)
    seller_id = models.UUIDField(max_length=36)
    product_code = models.TextField(max_length=64)
    gtin = models.TextField(max_length=14)
    name = models.TextField(max_length=128)
    status = models.TextField(max_length=64)
    brand = models.TextField(max_length=128)
    description = models.TextField()
    free_shipping = models.BooleanField()
    group_id = models.TextField(max_length=16)
    tax_information_id = models.UUIDField(null=True)
    approved = models.BooleanField()
    rejection_reasons = models.JSONField()
    active = models.BooleanField()
    part_number = models.TextField(max_length=32)
    in_campaign = models.BooleanField()
    odin = models.TextField(max_length=64)
    waiting_invoice = models.BooleanField()
    controller_gtin_id = models.UUIDField(null=True)
    currency = models.TextField(max_length=3)
    offer = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inactive_reason = models.TextField(max_length=64, null=True)
