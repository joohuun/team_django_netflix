# Generated by Django 3.2.5 on 2022-06-13 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenreModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'genre',
            },
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=256)),
                ('user_rate', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'comment',
            },
        ),
        migrations.CreateModel(
            name='MovieModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('url', models.CharField(blank=True, max_length=256, null=True)),
                ('imgurl', models.CharField(blank=True, max_length=256, null=True)),
                ('age', models.CharField(blank=True, max_length=256, null=True)),
                ('runningtime', models.CharField(blank=True, max_length=256, null=True)),
                ('opendate', models.CharField(blank=True, max_length=256, null=True)),
                ('actors', models.CharField(blank=True, max_length=256, null=True)),
                ('rate', models.FloatField(blank=True, null=True)),
                ('story', models.TextField(blank=True, null=True)),
                ('genre', models.ManyToManyField(related_name='genre', to='movie.GenreModel')),
            ],
            options={
                'db_table': 'movie',
            },
        ),
    ]
