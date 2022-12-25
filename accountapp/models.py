from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False) # null은 컬럼 디폴트 체크