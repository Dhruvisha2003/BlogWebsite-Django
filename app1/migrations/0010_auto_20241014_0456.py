# Generated by Django 3.2.12 on 2024-10-14 04:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_cmt'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmt',
            name='blog_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.blog'),
        ),
        migrations.AlterField(
            model_name='cmt',
            name='sub',
            field=models.CharField(max_length=100),
        ),
    ]
