# Generated by Django 3.2.4 on 2022-12-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('song_img', models.FileField(upload_to='')),
                ('singer', models.CharField(max_length=200)),
                ('song_file', models.FileField(upload_to='')),
            ],
        ),
    ]
