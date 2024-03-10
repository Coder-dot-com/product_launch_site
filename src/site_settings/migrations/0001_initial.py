# Generated by Django 5.0.3 on 2024-03-10 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_email', models.EmailField(blank=True, max_length=300, null=True)),
                ('site_logo', models.ImageField(blank=True, null=True, upload_to='logo/')),
                ('site_logo_square', models.ImageField(blank=True, null=True, upload_to='logo/')),
                ('site_name', models.CharField(blank=True, max_length=100, null=True)),
                ('site_slogan', models.CharField(blank=True, max_length=100, null=True)),
                ('site_icon', models.ImageField(blank=True, null=True, upload_to='logo/')),
                ('site_meta_tags', models.TextField(blank=True, max_length=2000, null=True)),
                ('site_global_analytics', models.TextField(blank=True, max_length=2000, null=True)),
                ('site_button_css', models.TextField(blank=True, max_length=2000, null=True)),
                ('site_button_hover_css', models.TextField(blank=True, max_length=2000, null=True)),
                ('site_button_focus_css', models.TextField(blank=True, max_length=2000, null=True)),
                ('site_secondary_button_css', models.TextField(blank=True, max_length=2000, null=True)),
                ('site_secondary_button_hover_css', models.TextField(blank=True, max_length=2000, null=True)),
                ('site_secondary_button_focus_css', models.TextField(blank=True, max_length=2000, null=True)),
                ('site_headings_css', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
