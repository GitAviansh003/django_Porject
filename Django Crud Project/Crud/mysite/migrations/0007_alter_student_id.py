# Generated by Django 4.2.5 on 2023-10-28 07:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
