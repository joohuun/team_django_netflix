# Generated by Django 4.0.5 on 2022-06-07 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_moviemodel_actors_alter_moviemodel_opendate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviemodel',
            name='post_img',
            field=models.ImageField(blank=True, upload_to='upload'),
        ),
    ]
