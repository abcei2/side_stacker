# Generated by Django 3.1.3 on 2021-03-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20210327_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporalgame',
            name='player_x',
            field=models.TextField(default='None', max_length=1024),
        ),
        migrations.AlterField(
            model_name='temporalgame',
            name='player_y',
            field=models.TextField(default='None', max_length=1024),
        ),
    ]
