# Generated by Django 2.2.7 on 2019-12-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('harga', models.IntegerField()),
                ('satuan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Warga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('komentar', models.CharField(max_length=800)),
            ],
        ),
    ]
