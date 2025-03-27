from django.db import models

# Create your models here.
# class cfr_reference(models.Model):
#     title = models.IntegerField()
#     chapter = models.CharField(default=50)

# class ChildAgency(models.Model):
#     name = models.CharField(max_length=100)
#     short_name = models.CharField(default=10)
#     display_name = models.CharField(default=100)
#     sortable_name = models.CharField(default=100)
#     slug = models.CharField(default=100)
#     cfr_reference = models.OneToOneField(cfr_reference, on_delete=models.CASCADE)

class Agency(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=10)
    display_name = models.CharField(max_length=100)
    sortable_name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    children = models.JSONField()
    cfr_references = models.JSONField()