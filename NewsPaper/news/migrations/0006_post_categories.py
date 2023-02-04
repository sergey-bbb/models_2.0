# Generated by Django 4.1.4 on 2023-02-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_delete_a_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(through='news.PostCategory', to='news.category'),
        ),
    ]