# Generated by Django 4.0 on 2021-12-10 13:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdf',
            name='key_words',
        ),
        migrations.RemoveField(
            model_name='pdf',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='pdf',
            name='period',
        ),
        migrations.AddField(
            model_name='pdf',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='PDF dosyası ekleyin'),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='pdf',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Başlık'),
        ),
    ]