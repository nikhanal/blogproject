# Generated by Django 3.0.6 on 2020-05-26 07:11

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(default=True),
            preserve_default=False,
        ),
    ]
