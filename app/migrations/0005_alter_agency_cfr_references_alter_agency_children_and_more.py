# Generated by Django 5.1.7 on 2025-03-27 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_cfr_references_cfrreferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='cfr_references',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cfrreferences'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='children',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.childagency'),
        ),
        migrations.AlterField(
            model_name='childagency',
            name='cfr_references',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cfrreferences'),
        ),
    ]
