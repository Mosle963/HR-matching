# Generated by Django 5.0.3 on 2024-04-18 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_remove_cluster_records_word2vec_word_min_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cluster_records',
            name='inertia',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
