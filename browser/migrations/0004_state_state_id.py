# Generated by Django 3.1.7 on 2021-03-09 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0003_auto_20210308_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='state_id',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]