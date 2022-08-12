# Generated by Django 4.1 on 2022-08-11 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leaveApi', '0002_delete_leave'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(auto_now=True, null=True)),
                ('date_to', models.DateField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('select', 'select'), ('pending  ', 'pending'), ('approved', 'approved'), ('cancel', 'cancel'), ('reject', 'reject')], default='select', max_length=20)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
