# Generated by Django 4.0.5 on 2022-06-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_alter_moviemodel_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
