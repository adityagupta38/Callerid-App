# Generated by Django 4.0.4 on 2022-09-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callinfo', '0002_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='spam',
            field=models.CharField(default='No', editable=False, max_length=3),
        ),
    ]
