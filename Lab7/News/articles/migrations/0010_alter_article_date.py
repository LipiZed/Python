# Generated by Django 3.2.18 on 2023-10-03 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_article_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]