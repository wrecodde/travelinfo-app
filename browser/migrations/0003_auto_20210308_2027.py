# Generated by Django 3.1.7 on 2021-03-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0002_auto_20210308_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal',
            name='dest_terminals',
            field=models.ManyToManyField(blank=True, related_name='_terminal_dest_terminals_+', to='browser.Terminal'),
        ),
    ]
