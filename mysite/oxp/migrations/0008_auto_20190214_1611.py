# Generated by Django 2.1.5 on 2019-02-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oxp', '0007_auto_20190214_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='images',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
