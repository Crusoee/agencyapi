# Generated by Django 5.1.7 on 2025-03-27 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='short_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
