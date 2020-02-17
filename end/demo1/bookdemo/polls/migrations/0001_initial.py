# Generated by Django 3.0.3 on 2020-02-16 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.CharField(max_length=50, null=True)),
                ('onenum', models.IntegerField(max_length=8, null=True)),
                ('two', models.CharField(max_length=50, null=True)),
                ('twonum', models.IntegerField(max_length=8, null=True)),
                ('three', models.CharField(max_length=50, null=True)),
                ('threenum', models.IntegerField(max_length=8, null=True)),
                ('four', models.CharField(max_length=50, null=True)),
                ('fournum', models.IntegerField(max_length=8, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question')),
            ],
        ),
    ]