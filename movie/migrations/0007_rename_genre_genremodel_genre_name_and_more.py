# Generated by Django 4.0.5 on 2022-06-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_alter_moviemodel_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genremodel',
            old_name='genre',
            new_name='genre_name',
        ),
        migrations.RemoveField(
            model_name='moviemodel',
            name='genre_name',
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='genre',
            field=models.ManyToManyField(to='movie.genremodel'),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='age',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='opendate',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='moviemodel',
            name='runningtime',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
