# Generated by Django 4.0.6 on 2022-08-03 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_remove_context_title_txt_heading_title_txt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='context',
            name='type',
            field=models.CharField(default='Django', max_length=10),
        ),
    ]