# Generated by Django 3.0.3 on 2020-02-25 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thunb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]