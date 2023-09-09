# Generated by Django 3.2.21 on 2023-09-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230908_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('animals', '動物を守る'), ('aquatic systems', '海、川、湖を守る'), ('soil & trees', '土と木を守る'), ('save resources', 'その他資源を守る'), ('eco-conscious life style', '環境に配慮したライフスタイル'), ('others', 'その他')], default='others', max_length=30),
        ),
    ]