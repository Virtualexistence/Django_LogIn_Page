# Generated by Django 4.0.6 on 2022-08-03 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_remove_heading_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='title_txt',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authapp.heading'),
        ),
    ]
