# Generated by Django 4.0.3 on 2022-03-21 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
