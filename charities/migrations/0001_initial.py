# Generated by Django 3.2.3 on 2021-07-12 11:23

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
            name='Benefactor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('experience', models.SmallIntegerField(choices=[(0, 'low'), (1, 'middle'), (2, 'high')], default=0)),
                ('free_time_per_week', models.PositiveSmallIntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('reg_number', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('age_limit_form', models.IntegerField(blank=True, null=True)),
                ('age_limit_to', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('gender_limit', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('state', models.CharField(choices=[('P', 'Pending'), ('W', 'Waiting'), ('A', 'Assigned'), ('D', 'Done')], default='D', max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('assigned_benefactor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='charities.benefactor')),
                ('charity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charities.charity')),
            ],
        ),
    ]