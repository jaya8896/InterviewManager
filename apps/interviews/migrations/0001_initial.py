# Generated by Django 2.2 on 2021-01-10 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=100)),
                ('value', models.TextField(max_length=3000)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InterviewerAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slot_start_time', models.DateTimeField()),
                ('slot_end_time', models.DateTimeField()),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actors.Interviewer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('is_completed', models.BooleanField(blank=True, default=False)),
                ('is_cancelled', models.BooleanField(blank=True, default=False)),
                ('cancelled_time', models.DateTimeField(blank=True, null=True)),
                ('grade', models.SmallIntegerField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('interviewer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actors.Interviewer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='actors.Student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
