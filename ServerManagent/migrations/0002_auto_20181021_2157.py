# Generated by Django 2.0.3 on 2018-10-21 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServerManagent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servermanagent',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
