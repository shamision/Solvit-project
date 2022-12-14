# Generated by Django 4.0.6 on 2022-07-15 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('imageUrl', models.URLField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('form', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='pForm', to='PoemApp.form')),
                ('genre', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='pGenre', to='PoemApp.genre')),
            ],
        ),
    ]
