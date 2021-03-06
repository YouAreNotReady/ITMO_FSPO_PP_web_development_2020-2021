# Generated by Django 3.1.7 on 2021-03-22 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=15)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AutoOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birthday_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(null=True)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.auto')),
                ('auto_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.autoowner')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('date', models.DateTimeField()),
                ('auto_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.autoowner')),
            ],
        ),
    ]
