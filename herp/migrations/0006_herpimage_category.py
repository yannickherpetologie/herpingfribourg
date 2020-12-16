# Generated by Django 3.1.4 on 2020-12-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herp', '0005_auto_20201215_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='herpimage',
            name='category',
            field=models.CharField(choices=[('I', 'Image'), ('M', 'MP3'), ('V', 'Video')], default='', max_length=1),
            preserve_default=False,
        ),
    ]