# Generated by Django 2.1.5 on 2019-02-14 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oxp', '0004_auto_20190214_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
