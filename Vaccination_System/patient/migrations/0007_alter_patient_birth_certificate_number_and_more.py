# Generated by Django 4.1.2 on 2022-10-16 15:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_alter_patient_doz1_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='birth_certificate_number',
            field=models.CharField(max_length=10, verbose_name='شماره شناسنامه'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doz1_time',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='تاریخ دریافت دوز اول'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='national_code',
            field=models.CharField(max_length=10, verbose_name='کد ملی'),
        ),
    ]