# Generated by Django 4.2.2 on 2023-09-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_bookstoremodel_last_pub'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookstoremodel',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='book_covers/'),
        ),
        migrations.AlterField(
            model_name='bookstoremodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
