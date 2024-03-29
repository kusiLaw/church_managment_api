# Generated by Django 5.0 on 2023-07-28 22:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-create_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-create_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('theme', models.CharField(blank=True, help_text='Theme of the event or church programs', max_length=100, null=True)),
                ('image', models.ImageField(upload_to='church/static/events/')),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('location', models.CharField(max_length=100)),
                ('speaker', models.CharField(max_length=100)),
                ('guss_speaker', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('occupation', models.CharField(blank=True, max_length=45, null=True)),
                ('postal_code', models.CharField(max_length=20)),
                ('address_line', models.CharField(max_length=25)),
                ('date_baptized', models.DateField(blank=True, help_text='Date Object. Helps to determined if a user is                                     considered as member of the church ', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leadership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.department')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.membership')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date', models.DateField()),
                ('dues', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.dues')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='church.membership')),
            ],
        ),
    ]
