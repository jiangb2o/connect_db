from django.db import models

import psycopg2

# # psycopg2常用链接方式
# conn = psycopg2.connect(dbname="postgres", user="user", password="password", host="localhost", port=port)

# # 创建连接对象
# conn=psycopg2.connect(database="postgres",user="user",password="password",host="localhost",port=port)
# cur=conn.cursor() #创建指针对象

# # 创建连接对象（SSl连接）
# conn = psycopg2.connect(dbname="postgres", user="user", password="password", host="localhost", port=port,
#          sslmode="verify-ca", sslcert="client.crt",sslkey="client.key",sslrootcert="cacert.pem")
# #注意： 如果sslcert, sslkey,sslrootcert没有填写，默认取当前用户.postgresql目录下对应的client.crt，client.key， root.crt

# # 创建表
# cur.execute("CREATE TABLE student(id integer,name varchar,sex varchar);")

# # 插入数据
# cur.execute("INSERT INTO student(id,name,sex) VALUES(%s,%s,%s)",(1,'Aspirin','M'))
# cur.execute("INSERT INTO student(id,name,sex) VALUES(%s,%s,%s)",(2,'Taxol','F'))
# cur.execute("INSERT INTO student(id,name,sex) VALUES(%s,%s,%s)",(3,'Dixheral','M'))

# # 获取结果
# cur.execute('SELECT * FROM student')
# results=cur.fetchall()
# print (results)

# # 关闭连接
# conn.commit()
# cur.close()
# conn.close()


class Patient(models.Model):
    '''病人'''
    name = models.CharField(verbose_name='姓名', max_length = 20)
    age = models.IntegerField(verbose_name='年龄', null=True, blank=True)
    username = models.CharField(verbose_name='用户名', max_length = 20)
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
    username = models.CharField(verbose_name='用户名', max_length = 20)
    password = models.CharField(verbose_name='密码', max_length = 20)
    title = models.CharField(verbose_name='职称', max_length = 20)
    dept = models.ForeignKey(to=Department, to_field='id', on_delete=models.CASCADE)

class Registration(models.Model):
    '''挂号记录'''

    # class Meta:
    #     verbose_name = '挂号记录'
    #     verbose_name_plural = '挂号记录'

    STATUS_CHOICES = [
        ('registered', '已挂号'),
        ('cancelled', '已取消'),
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
    peirod = models.SmallIntegerField(verbose_name='挂号时段', choices=PERIOD_CHOICES)
    status = models.CharField(verbose_name='状态', max_length=10, choices=STATUS_CHOICES)