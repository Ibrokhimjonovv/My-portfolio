# Generated by Django 4.2.5 on 2023-09-26 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_skills_name_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='percent',
            field=models.IntegerField(default=0),
        ),
    ]
