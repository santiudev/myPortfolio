# Generated by Django 3.0.1 on 2022-11-23 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='projects'),
        ),
    ]
