# Generated by Django 3.2.7 on 2021-09-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='age',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='date_ctrated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='medic',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='sex',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='surname',
            field=models.CharField(max_length=255),
        ),
    ]