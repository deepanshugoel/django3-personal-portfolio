# Generated by Django 3.1.6 on 2021-02-14 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogging',
            name='image',
        ),
        migrations.RemoveField(
            model_name='blogging',
            name='url',
        ),
        migrations.AddField(
            model_name='blogging',
            name='datess',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
