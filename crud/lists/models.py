from django.db import models
import uuid

# Create your models here.

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200,null=True)
    capital = models.CharField(max_length=200)
    citizenship = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    currency_code = models.CharField(max_length=200)

    class Meta:
        db_table = 'tab_countries'