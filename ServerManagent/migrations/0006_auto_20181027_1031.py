# Generated by Django 2.0.3 on 2018-10-27 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ServerManagent', '0005_auto_20181027_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servermanagent',
            name='status',
            field=models.CharField(choices=[('ON', '运行'), ('stopping', '准备停'), ('stoped', '已停'), ('free', '免费')], default='ON', max_length=10),
        ),
    ]