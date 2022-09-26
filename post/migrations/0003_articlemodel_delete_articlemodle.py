# Generated by Django 4.1 on 2022-09-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_articlemodle_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='ArticleModle',
        ),
    ]
