# Generated by Django 4.0 on 2021-12-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0004_alter_pdf_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdf',
            name='content',
            field=models.CharField(max_length=5000, verbose_name='İçerik'),
        ),
    ]
