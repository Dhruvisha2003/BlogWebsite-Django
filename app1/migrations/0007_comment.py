# Generated by Django 3.2.12 on 2024-10-11 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_alter_myprofile_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=20)),
                ('sub', models.CharField(blank=True, max_length=100, null=True)),
                ('msg', models.CharField(max_length=500)),
            ],
        ),
    ]