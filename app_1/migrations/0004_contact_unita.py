# Generated by Django 2.2.7 on 2019-12-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0003_auto_20191210_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='unita',
            field=models.CharField(choices=[('gradi centigradi', 'gradi centigradi'), ('gradi farenight', 'gradi farenight')], default=0, max_length=200),
            preserve_default=False,
        ),
    ]
