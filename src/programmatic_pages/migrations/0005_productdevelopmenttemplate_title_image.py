# Generated by Django 5.0.3 on 2024-03-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmatic_pages', '0004_productdevelopmenttemplate_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdevelopmenttemplate',
            name='title_image',
            field=models.ImageField(blank=True, null=True, upload_to='resources/templates/'),
        ),
    ]