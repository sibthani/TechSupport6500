# Generated by Django 3.1.1 on 2021-07-23 18:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('supportapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issue_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
