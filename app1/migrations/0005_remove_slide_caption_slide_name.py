# Generated by Django 5.0.3 on 2024-10-11 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_myprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='caption',
        ),
        migrations.AddField(
            model_name='slide',
            name='name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.category'),
        ),
    ]