# Generated by Django 5.0.3 on 2024-03-17 13:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmatic_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdevelopmenttemplate',
            name='keyword',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='programmatic_pages.keyword'),
        ),
        migrations.AlterField(
            model_name='productdevelopmenttemplate',
            name='meta_description',
            field=models.TextField(max_length=500),
        ),
    ]
