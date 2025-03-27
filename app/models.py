from django.db import models

# Create your models here.
class cfr_reference(models.Model):
    title = models.IntegerField(null=True, blank=True)
    chapter = models.CharField(max_length=50, null=True, blank=True)

class ChildAgency(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    short_name = models.CharField(max_length=10,null=True, blank=True)
    display_name = models.CharField(max_length=100, null=True, blank=True)
    sortable_name = models.CharField(max_length=100, null=True, blank=True)
    slug = models.CharField(max_length=100, null=True, blank=True)
    cfr_reference = models.OneToOneField(cfr_reference, on_delete=models.CASCADE)

class Agency(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10, null=True, blank=True)
    display_name = models.CharField(max_length=100)
    sortable_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    children = models.JSONField()
    cfr_references = models.JSONField()