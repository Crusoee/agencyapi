# Generated by Django 5.1.7 on 2025-03-27 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_agency_cfr_references_alter_agency_children_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='cfr_references',
            field=models.JSONField(),
        ),
        migrations.RemoveField(
            model_name='childagency',
            name='cfr_references',
        ),
        migrations.AlterField(
            model_name='agency',
            name='children',
            field=models.JSONField(),
        ),
        migrations.DeleteModel(
            name='CfrReferences',
        ),
        migrations.DeleteModel(
            name='ChildAgency',
        ),
    ]
