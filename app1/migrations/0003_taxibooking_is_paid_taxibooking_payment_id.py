# Generated by Django 4.2.9 on 2024-04-02 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_registeration_city_registeration_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxibooking',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='taxibooking',
            name='payment_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
