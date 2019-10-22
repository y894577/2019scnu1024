from django.db import models
import django.utils.timezone as timezone

class STUDB(models.Model):
    userid = models.TextField(max_length=11)
    username = models.TextField(max_length=10)
    passwd = models.TextField(max_length=20)
    # 1-6关开始结束时间
    firstflag = models.DateTimeField(default=timezone.now)
    lastflag = models.DateTimeField(default=timezone.now)
    # 最后一关的时间
    superflag = models.DateTimeField(default=timezone.now)
    # 彩蛋的时间
    specialflag = models.DateTimeField(default=timezone.now)
    # rank记录
    rank = models.IntegerField(default=1)
    # 时间差
    timesubtract = models.IntegerField(default=0)

    def __str__(self):
        return self.userid

# class Encryption(models.Model):
#     student = models.ForeignKey(STU,on_delete=models.CASCADE)
#     # 此处需要进行md5加密
#     flag = models.TextField()
#
#     def __str__(self):
#         return self.STU
