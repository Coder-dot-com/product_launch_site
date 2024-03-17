# Generated by Django 5.0.3 on 2024-03-17 13:34

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpage_generate_title_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.fields.StreamField([('article_section', wagtail.blocks.StructBlock([('header', wagtail.blocks.CharBlock(required=False)), ('content', wagtail.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'strikethrough', 'blockquote'], required=False))]))]),
        ),
    ]