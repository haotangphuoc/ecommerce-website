# Generated by Django 4.1.3 on 2023-01-02 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='province',
            field=models.CharField(default='Nova Scotia', max_length=2),
        ),
    ]
