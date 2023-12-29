from django.db import models

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
    room_number = models.CharField(verbose_name='房间号', max_length = 20)

class Doctor(models.Model):
    '''医生'''
    name = models.CharField(verbose_name='姓名', max_length = 20)
    username = models.CharField(verbose_name='用户名', max_length = 20, unique=True)
    password = models.CharField(verbose_name='密码', max_length = 20)
    title = models.CharField(verbose_name='职称', max_length = 20)
    dept = models.ForeignKey(Department, verbose_name='科室', on_delete=models.CASCADE)
    profile = models.CharField(verbose_name='简介', max_length = 200)


class Registration(models.Model):
    '''挂号记录'''

    # class Meta:
    #     verbose_name = '挂号记录'
    #     verbose_name_plural = '挂号记录'

    STATUS_CHOICES = [
        (0, '已挂号'),
        (1, '已取消'),
        (2, '就诊中'),
        (3, '就诊结束'),
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
    status = models.SmallIntegerField(verbose_name='状态', choices=STATUS_CHOICES)

class MedicalRecord(models.Model):
    '''病历'''
    symptom = models.CharField(verbose_name='症状', max_length = 200)
    diagnosis = models.CharField(verbose_name='诊断结果', max_length = 200)
    solution = models.CharField(verbose_name='治疗方案', max_length = 200)
    registration = models.ForeignKey(Registration, verbose_name='预约信息', on_delete=models.CASCADE)


class Medicine(models.Model):
    '''药物'''
    TYPE_CHOICES = [
        (0, '中药'),
        (1, '西药'),
    ]

    name = models.CharField(verbose_name='名称', max_length = 100)
    type = models.SmallIntegerField(verbose_name='类型', choices=TYPE_CHOICES)
    producer = models.CharField(verbose_name='生产厂商', max_length = 100)
    price = models.DecimalField(verbose_name='价格', max_digits=5, decimal_places=2)