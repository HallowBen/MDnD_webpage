# Generated by Django 4.1 on 2022-08-15 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_rating_comment_alter_rating_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='bname',
            new_name='r_bname',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='fname',
            new_name='r_fname',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='comment',
            new_name='r_message',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='sname',
            new_name='r_sname',
        ),
    ]
