# Generated by Django 3.1.1 on 2021-03-01 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('handlers', '0003_auto_20210221_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='handler',
            name='expire_on_inactivity_of',
            field=models.IntegerField(default=300),
        ),
        migrations.AddField(
            model_name='handler',
            name='last_accessed_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='handler',
            name='trigger_word',
            field=models.CharField(default='USSD', max_length=50),
        ),
        migrations.AlterField(
            model_name='handler',
            name='auth_scheme',
            field=models.CharField(default='TOKEN', max_length=30),
        ),
    ]