# Generated by Django 2.2.6 on 2019-12-29 07:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='code',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='Code'),
        ),
    ]