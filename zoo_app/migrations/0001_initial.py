# Generated by Django 5.0.1 on 2024-01-23 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('sug_haya', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=20)),
            ],
        ),
    ]