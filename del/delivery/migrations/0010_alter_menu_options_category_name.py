# Generated by Django 4.1.7 on 2023-03-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0009_menu_url_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
