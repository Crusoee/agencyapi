# Generated by Django 5.1.7 on 2025-03-27 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_childagency_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childagency',
            name='short_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
