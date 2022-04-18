# Generated by Django 4.0.3 on 2022-03-17 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hosapp', '0003_delete_doctors_tb_delete_patient_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=200)),
                ('specailised', models.CharField(max_length=200)),
                ('available', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='patient_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
                ('about', models.CharField(max_length=200)),
            ],
        ),
    ]
