from django.contrib.gis.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)




class Counties(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __unicode__(self):
    	return self.counties

    class Meta:
        verbose_name_plural = 'Counties'
