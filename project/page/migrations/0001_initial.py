# Generated by Django 3.1.4 on 2020-12-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Html_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='')),
                ('upload_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_id', models.CharField(default='', max_length=50)),
                ('User_pw', models.CharField(max_length=100)),
                ('User_name', models.CharField(max_length=25)),
            ],
        ),
    ]
