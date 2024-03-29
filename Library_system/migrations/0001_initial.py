# Generated by Django 3.2 on 2022-03-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=255)),
                ('book_num', models.PositiveIntegerField()),
                ('added_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
