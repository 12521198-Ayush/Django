# Generated by Django 4.2 on 2023-05-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_remove_student_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='attendance',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
