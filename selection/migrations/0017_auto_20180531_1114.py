# Generated by Django 2.0.5 on 2018-05-31 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0016_auto_20180531_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel',
            name='course',
            field=models.CharField(blank=True, choices=[('IT', 'Information Technology'), ('ECE', 'Electronics and Communication')], default=None, max_length=5, null=True),
        ),
    ]
