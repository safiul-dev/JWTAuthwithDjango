# Generated by Django 3.2.7 on 2021-09-04 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=59, null=True)),
                ('text', models.CharField(max_length=200, null=True)),
                ('userId', models.IntegerField(null=True)),
            ],
        ),
    ]
