# Generated by Django 2.2 on 2019-04-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', '♂'), ('F', '♀')], max_length=1),
        ),
        migrations.AlterField(
            model_name='master',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', '♂'), ('F', '♀')], max_length=1),
        ),
    ]
