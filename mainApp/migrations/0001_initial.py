# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-11-04 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passwords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field_name', models.CharField(help_text='Enter field documentation', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_ID', models.CharField(max_length=20)),
                ('urlNAME', models.CharField(max_length=20)),
                ('websiteName', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Users')),
            ],
        ),
        migrations.AddField(
            model_name='passwords',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Users'),
        ),
        migrations.AddField(
            model_name='passwords',
            name='websiteID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Website'),
        ),
    ]
