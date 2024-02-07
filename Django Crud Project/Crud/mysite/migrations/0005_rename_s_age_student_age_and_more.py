# Generated by Django 4.2.5 on 2023-10-28 06:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_alter_student_s_age_alter_student_s_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='s_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='s_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='s_gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='s_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
