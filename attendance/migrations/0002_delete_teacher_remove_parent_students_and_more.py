# Generated by Django 4.2 on 2023-05-09 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='students',
        ),
        migrations.AddField(
            model_name='parent',
            name='child_name',
            field=models.CharField(default=1234, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='attendance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.CharField(max_length=20),
        ),
    ]