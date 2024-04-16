# Generated by Django 5.0.4 on 2024-04-16 18:04

import django.core.validators
import final_project.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), final_project.core.validators.validate_only_letters, final_project.core.validators.validate_start_with_capital_letter])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), final_project.core.validators.validate_only_letters, final_project.core.validators.validate_start_with_capital_letter])),
                ('image', models.URLField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
