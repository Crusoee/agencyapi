from django.db import models

# Create your models here.

class CfrReference(models.Model):
    title = models.IntegerField(null=True, blank=True)
    chapter = models.CharField(max_length=50, null=True, blank=True)

class Agency(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10, null=True, blank=True)
    display_name = models.CharField(max_length=100)
    sortable_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    cfr_references = models.ManyToManyField(CfrReference, related_name="agencies", blank=True)

    def __str__(self):
        return self.name
