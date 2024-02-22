# Generated by Django 4.1.13 on 2024-02-21 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asap', '0005_generateddata_theme_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_image', models.ImageField(blank=True, upload_to='text_image')),
                ('background_image', models.ImageField(blank=True, upload_to='background_image')),
                ('result_image_url', models.ImageField(blank=True, upload_to='result_image')),
            ],
        ),
    ]
