# Generated by Django 5.1.2 on 2024-10-20 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_blogmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogmodel',
            options={'verbose_name': 'blog', 'verbose_name_plural': 'Blogs'},
        ),
    ]
