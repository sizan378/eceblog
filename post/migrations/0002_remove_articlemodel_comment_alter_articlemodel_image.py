# Generated by Django 4.1 on 2022-10-31 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlemodel',
            name='comment',
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='image',
            field=models.ImageField(upload_to='image', verbose_name='Image'),
        ),
    ]