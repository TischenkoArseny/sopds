# Generated by Django 4.1.1 on 2022-09-13 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opds_catalog', '0007_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='theme_css',
            field=models.CharField(default='css/sopds.css', max_length=64),
        ),
    ]
