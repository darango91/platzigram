# Generated by Django 2.2.5 on 2019-09-19 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190918_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(related_name='followees', to='users.Profile'),
        ),
    ]
