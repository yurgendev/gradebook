# Generated by Django 5.0 on 2024-01-17 12:36

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('users', '0002_alter_parent_email_alter_student_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(db_index=True, max_length=50, unique=True)),
                ('english_group', models.ManyToManyField(related_name='english_groups', to='users.student')),
                ('students', models.ManyToManyField(related_name='classes', to='users.student')),
                ('ukrainian_group', models.ManyToManyField(related_name='ukrainian_groups', to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('grade_type', models.CharField(choices=[('homework', 'Homework'), ('test', 'Test'), ('exam', 'Exam')], max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='GradeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.parent')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.grade')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('subject', models.CharField(max_length=100)),
                ('class_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='schedule.class')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.lesson'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.lesson')),
            ],
        ),
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
                ('description', models.TextField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.lesson')),
            ],
        ),
    ]