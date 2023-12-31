# Generated by Django 3.2.21 on 2023-09-08 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_status',
            field=models.IntegerField(choices=[(0, 'オリジナル'), (1, '編集済み'), (2, '削除済み')], default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('animals', '動物を守る'), ('aquatic systems', '海、川、湖を守る'), ('soil & trees', '土と木を守る'), ('save resources', 'その他資源を守る'), ('eco-conscious life style', '環境に配慮した生活'), ('others', 'その他')], default='others', max_length=30),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, '投稿前'), (1, '投稿済み')], default=0),
        ),
    ]
