# Generated by Django 3.0.5 on 2021-02-15 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20210215_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
