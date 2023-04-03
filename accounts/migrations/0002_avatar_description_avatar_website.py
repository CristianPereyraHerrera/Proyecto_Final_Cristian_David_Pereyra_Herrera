# Generated by Django 4.1.7 on 2023-04-03 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='avatar',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
