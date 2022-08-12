# Generated by Django 4.1 on 2022-08-12 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaveApi', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='status',
            field=models.CharField(choices=[('select', 'select'), ('pending', 'pending'), ('approved', 'approved'), ('cancel', 'cancel'), ('reject', 'reject')], default='select', max_length=20),
        ),
    ]