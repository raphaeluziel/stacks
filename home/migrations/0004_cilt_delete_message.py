# Generated by Django 5.0.6 on 2024-07-02 13:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_message_delete_vehicle_delete_vehicletype'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cilt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_place', models.CharField(blank=True, max_length=200, null=True, verbose_name='Birth Place')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
