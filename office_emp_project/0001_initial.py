# Generated by Django 5.1.7 on 2025-03-24 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='General', max_length=100)),
                ('location', models.CharField(default='General', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('salary', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('hire_date', models.DateField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_employees', to='employee_app.department')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role_employees', to='employee_app.role')),
            ],
        ),
    ]
