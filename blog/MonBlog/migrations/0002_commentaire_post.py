# Generated by Django 3.1.7 on 2021-03-05 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MonBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MonBlog.post'),
        ),
    ]
