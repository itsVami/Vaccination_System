# Generated by Django 4.1.2 on 2022-10-19 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0003_alter_vaccine_count_category_vaccine_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(verbose_name='انتشار داده شود؟'),
        ),
    ]