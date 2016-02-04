# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
                  migrations.CreateModel(
                                         name='City',
                                         fields=[
                                                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                                                 ('city_name', models.CharField(max_length=200)),
                                                 ('length_of_stay', models.IntegerField(default=0)),
                                                 ],
                                         ),
                  migrations.CreateModel(
                                         name='Country',
                                         fields=[
                                                 ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                                                 ('country_name', models.CharField(max_length=200)),
                                                 ('favorite_local_food', models.CharField(max_length=200)),
                                                 ('favorite_tourist_spot', models.CharField(max_length=200)),
                                                 ('date_visited', models.DateField(verbose_name=b'date visited')),
                                                 ],
                                         ),
                  migrations.AddField(
                                      model_name='city',
                                      name='country_name',
                                      field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Country'),
                                      ),
    ]
