# Generated by Django 4.1.7 on 2023-04-01 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=45)),
                ('lname', models.CharField(max_length=45)),
                ('mobile', models.BigIntegerField()),
                ('email', models.CharField(max_length=45)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LoginAPP.city')),
                ('course_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LoginAPP.course')),
            ],
        ),
    ]