# Generated by Django 2.2.7 on 2019-12-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0005_auto_20191211_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='unita',
            field=models.CharField(choices=[('gradi centigradi', 'gradi centigradi'), ('gradi fahrenheit', 'gradi fahrenheit')], max_length=200),
        ),
    ]
