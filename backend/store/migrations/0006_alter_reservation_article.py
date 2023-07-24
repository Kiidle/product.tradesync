# Generated by Django 4.1.7 on 2023-07-23 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_article_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='store.article'),
        ),
    ]
