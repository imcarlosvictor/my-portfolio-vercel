# Generated by Django 4.0.6 on 2022-10-12 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_portfolio', '0019_alter_project_tech_stack'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='programming_languages',
        ),
    ]
