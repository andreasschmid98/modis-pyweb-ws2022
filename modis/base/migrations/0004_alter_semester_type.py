# Generated by Django 4.1.3 on 2022-12-21 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_graduateprogram_degree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='type',
            field=models.CharField(choices=[('Wintersemester', 'Winter'), ('Sommersemester', 'Summer')], max_length=20),
        ),
    ]
