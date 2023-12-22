# Generated by Django 5.0 on 2023-12-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_alter_user_about_me_alter_user_grade_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(max_length=20, verbose_name="이름"),
        ),
        migrations.AlterField(
            model_name="user",
            name="profile_picture",
            field=models.ImageField(
                blank=True, upload_to="profile_pics/", verbose_name="프로필 사진"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=30, unique=True, verbose_name="아이디"),
        ),
    ]
