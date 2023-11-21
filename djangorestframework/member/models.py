from django.db import models
from utils.models import BaseTimeEntity


# Create your models here.
class Member(BaseTimeEntity):
    # id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)

    class Meta:
        db_table = "user"
