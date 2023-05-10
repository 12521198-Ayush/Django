# Generated by Django 4.2 on 2023-05-10 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_student_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='parent',
            name='child_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='attendance',
        ),
        migrations.AddField(
            model_name='parent',
            name='children',
            field=models.ManyToManyField(related_name='parents', to='attendance.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.CharField(max_length=10),
        ),
    ]