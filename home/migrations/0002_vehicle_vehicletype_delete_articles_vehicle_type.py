# Generated by Django 5.0.6 on 2024-06-14 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('farekm', models.FloatField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Articles',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.vehicletype'),
        ),
    ]