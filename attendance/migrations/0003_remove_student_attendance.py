# Generated by Django 4.2 on 2023-05-09 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_delete_teacher_remove_parent_students_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='attendance',
        ),
    ]
