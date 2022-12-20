# Generated by Django 4.1.3 on 2022-12-10 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='favourites',
            field=models.ManyToManyField(to='base.module'),
        ),
        migrations.AlterField(
            model_name='module',
            name='lecturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.lecturer'),
        ),
    ]