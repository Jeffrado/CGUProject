# Generated by Django 2.0.2 on 2018-04-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_phrase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='singer',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]