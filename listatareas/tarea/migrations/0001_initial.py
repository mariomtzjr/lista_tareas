# Generated by Django 2.0.9 on 2019-02-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='creaTarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-creacion'],
            },
        ),
    ]