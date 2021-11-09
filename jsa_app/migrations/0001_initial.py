# Generated by Django 3.2.9 on 2021-11-09 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('choices', models.CharField(choices=[('Yes', 'Y'), ('No', 'N'), ('NA', 'NA')], max_length=50)),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsa_app.checklist')),
            ],
        ),
        migrations.CreateModel(
            name='JSAChecklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jsa_app.checklist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
