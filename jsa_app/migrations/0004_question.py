# Generated by Django 3.2.9 on 2021-11-09 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jsa_app', '0003_auto_20211109_1809'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('choice', models.CharField(choices=[('Yes', 'Y'), ('No', 'N'), ('NA', 'NA')], max_length=30)),
            ],
        ),
    ]