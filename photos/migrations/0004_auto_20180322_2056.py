# Generated by Django 2.0.1 on 2018-03-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_pic_horizontal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='horizontal',
            field=models.BooleanField(default=True),
        ),
    ]
