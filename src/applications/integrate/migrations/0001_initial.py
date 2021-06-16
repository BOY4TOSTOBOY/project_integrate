# Generated by Django 3.1 on 2021-06-15 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RepositoryGithub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branches_name', models.CharField(max_length=30)),
                ('sha', models.CharField(max_length=100)),
                ('display_id', models.CharField(max_length=30)),
                ('url_repository', models.CharField(max_length=255)),
                ('author_commit', models.CharField(max_length=30)),
                ('commit_message', models.CharField(blank=True, max_length=255)),
                ('stats_commit_add', models.IntegerField(blank=True)),
                ('stats_commit_delete', models.IntegerField(blank=True)),
                ('stats_commit_change', models.IntegerField(blank=True)),
                ('file_name', models.CharField(blank=True, max_length=40)),
                ('full_path_to_file', models.CharField(blank=True, max_length=255)),
                ('file_status', models.CharField(blank=True, max_length=15)),
                ('blame_hash_commit', models.CharField(blank=True, max_length=20)),
                ('blame_author_commit', models.CharField(blank=True, max_length=30)),
                ('blame_date_last_change', models.CharField(blank=True, max_length=11)),
                ('blame_code', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_text', models.CharField(help_text='Enter your url address, for example https://github.com/apache/hadoop.git', max_length=255)),
                ('commit_hash', models.CharField(max_length=50)),
            ],
        ),
    ]
