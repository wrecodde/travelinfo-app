# Generated by Django 3.1.7 on 2021-03-09 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('browser', '0007_auto_20210309_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='browser.state'),
        ),
    ]
