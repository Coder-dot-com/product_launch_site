# Generated by Django 5.0.3 on 2024-03-16 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='generate_title_image',
            field=models.BooleanField(default=False),
        ),
    ]