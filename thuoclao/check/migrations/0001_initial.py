# Generated by Django 2.0.4 on 2018-07-20 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email_alert', models.EmailField(blank=True, max_length=100)),
                ('telegram_id', models.CharField(blank=True, help_text='Telegram ID', max_length=10)),
                ('webhook', models.URLField(blank=True, help_text='URL to send message into Slack.')),
                ('delay_check', models.IntegerField(default=10, help_text='Interval time to check status host. - unit: second')),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True, null=True)),
                ('ok', models.IntegerField(blank=True, null=True)),
                ('warning', models.IntegerField(blank=True, null=True)),
                ('critical', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Group_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=45)),
                ('value', models.CharField(max_length=100)),
                ('type_value', models.IntegerField(help_text='0: integer, 1: bool, 2: date, 3: string, 4: ip-domain, 5: URL', null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=45)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(default=-1, help_text='0: ok, 1: warning, 2: critical')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.Group')),
            ],
            options={
                'ordering': ('hostname',),
            },
        ),
        migrations.CreateModel(
            name='Host_attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=45)),
                ('value', models.CharField(max_length=100)),
                ('type_value', models.IntegerField(help_text='0: integer, 1: bool, 2: date, 3: string, 4: ip-domain, 5: URL', null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ('service_name',),
            },
        ),
        migrations.AddField(
            model_name='group',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='check.Service'),
        ),
        migrations.AddField(
            model_name='group',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
