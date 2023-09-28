# Generated by Django 4.2.5 on 2023-09-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_skills_class_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=32)),
                ('percent', models.IntegerField(default=0)),
            ],
        ),
    ]