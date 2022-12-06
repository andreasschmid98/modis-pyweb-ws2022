# Generated by Django 4.1.3 on 2022-12-05 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'lecturer'), (2, 'student'), (3, 'admin')]),
        ),
    ]