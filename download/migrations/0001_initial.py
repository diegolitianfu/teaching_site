# Generated by Django 2.1.1 on 2019-03-13 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileSto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cata', models.CharField(choices=[('lunwen', '论文'), ('sheji', '设计报告参考'), ('kejian', '课件'), ('qita', '其他')], default='qita', max_length=20, verbose_name='文件类别')),
                ('file', models.FileField(upload_to='files/', verbose_name='文件选择')),
            ],
        ),
    ]