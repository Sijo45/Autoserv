# Generated by Django 3.1.3 on 2023-05-01 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_service', '0014_auto_20230501_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carbrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carbrand', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carmodel', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
