# Generated by Django 5.1.5 on 2025-01-27 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_post_options_news_post_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='News_post',
            new_name='New_post',
        ),
    ]
