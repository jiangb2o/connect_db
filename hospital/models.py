from django.db import models

import psycopg2

class Patient(models.Model):
    '''病人'''
    name = models.CharField(verbose_name='姓名', max_length = 20)
    age = models.IntegerField(verbose_name='年龄', null=True, blank=True)
    username = models.CharField(verbose_name='用户名', max_length = 20, unique=True)
    password = models.CharField(verbose_name='密码', max_length = 20)
    GENDER_CHOICES = [
        (0, '男'),
        (1, '女'),
    ]
    gender = models.SmallIntegerField(verbose_name='性别', choices=GENDER_CHOICES, null=True, blank=True)

class Department(models.Model):
    '''科室'''
    name = models.CharField(verbose_name='科室名', max_length = 30)

class Doctor(models.Model):
    '''医生'''
    name = models.CharField(verbose_name='姓名', max_length = 20)
    username = models.CharField(verbose_name='用户名', max_length = 20, unique=True)
    password = models.CharField(verbose_name='密码', max_length = 20)
    title = models.CharField(verbose_name='职称', max_length = 20)
    dept = models.ForeignKey(to=Department, to_field='id', on_delete=models.CASCADE)

class Registration(models.Model):
    '''挂号记录'''

    # class Meta:
    #     verbose_name = '挂号记录'
    #     verbose_name_plural = '挂号记录'

    STATUS_CHOICES = [
    ('Registered', '已挂号'),
    ('Cancelled', '已取消'),
    ('Processing', '就诊中'),
    ('Finished', '就诊结束'),
    ]

    PERIOD_CHOICES = [
        (0, '8:00-10:00'),
        (1, '10:00-12:00'),
        (2, '14:00-16:00'),
        (3, '16:00-18:00'),
    ]

    doctor = models.ForeignKey(Doctor, verbose_name='医生', on_delete=models.CASCADE, related_name='registrations')
    patient = models.ForeignKey(Patient, verbose_name='患者', on_delete=models.CASCADE, related_name='appointments')
    registration_time = models.DateTimeField(verbose_name='挂号时间')
    period = models.SmallIntegerField(verbose_name='挂号时段', choices=PERIOD_CHOICES)
    status = models.CharField(verbose_name='状态', max_length=10, choices=STATUS_CHOICES)