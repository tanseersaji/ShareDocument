# Generated by Django 3.2.5 on 2021-07-04 11:07

from django.db import migrations, models
import hashid_field.field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', hashid_field.field.HashidAutoField(alphabet='0123456789abcdefghijklmnopqrstuvwxyz', min_length=4, prefix='', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Document name')),
                ('document', models.FileField(upload_to='document', verbose_name='Document')),
            ],
        ),
    ]
