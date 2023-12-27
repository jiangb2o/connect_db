# Generated by Django 3.0 on 2023-12-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_auto_20231227_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicalrecord',
            old_name='symtom',
            new_name='symptom',
        ),
        migrations.AlterField(
            model_name='registration',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '已挂号'), (1, '已取消'), (2, '就诊中'), (3, '就诊结束')], verbose_name='状态'),
        ),
    ]
