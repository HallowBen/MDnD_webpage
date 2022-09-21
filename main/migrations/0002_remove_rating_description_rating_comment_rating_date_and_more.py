# Generated by Django 4.1 on 2022-08-15 12:24

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='description',
        ),
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='rating',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]