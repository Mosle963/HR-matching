# Generated by Django 5.0.3 on 2024-04-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_rename_ml_record_cluster_records'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cluster_records',
            name='end_date',
        ),
        migrations.AddField(
            model_name='cluster_records',
            name='applied',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
