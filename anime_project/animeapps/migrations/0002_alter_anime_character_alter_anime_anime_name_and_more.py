# Generated by Django 4.0.5 on 2022-07-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animeapps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='Character',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='anime',
            name='anime_name',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='profile_pic',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
