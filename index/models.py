from django.db import models
# Create your models here.

class gameInfo(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    bestPrice = models.FloatField()
    bestPriceCountry = models.CharField(max_length=10)
    platform = models.CharField(max_length=20)
    sellDate = models.DateField()
    devCompany = models.CharField(max_length=30)
    grade = models.IntegerField()

class gRadio(models.Model):
    head = models.CharField(max_length=50)
    time = models.DateField()
    href = models.URLField()
    imgSrc = models.URLField()
    imgTitle = models.CharField(max_length=50)
    describe = models.CharField(max_length=500)