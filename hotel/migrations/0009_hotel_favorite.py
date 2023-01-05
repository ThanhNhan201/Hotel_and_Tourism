# Generated by Django 2.2.1 on 2021-12-19 16:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0008_remove_booking_mess'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
