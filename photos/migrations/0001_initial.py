# Generated by Django 2.0.1 on 2018-03-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('body', models.TextField(null=True)),
                ('postDate', models.DateTimeField()),
                ('path', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='')),
                ('date', models.DateTimeField()),
                ('dimensions', models.CharField(max_length=60)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('flash', models.BooleanField()),
                ('focalLength', models.IntegerField()),
                ('whiteBalance', models.CharField(max_length=20)),
                ('aperture', models.FloatField()),
                ('exposure', models.CharField(max_length=40)),
                ('iso', models.IntegerField()),
                ('cameraModel', models.CharField(max_length=40)),
                ('editedParams', models.CharField(max_length=400)),
            ],
        ),
    ]
