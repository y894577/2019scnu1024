# must occur at the beginning of the file
from __future__ import unicode_literals
import hashlib
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from .models import STUDB
from functools import wraps
from django.contrib import messages
import re
from apps.shop.models import STUDB
import json


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def check_user(request):
    id = request.POST.get('id', None)
    passwd = request.POST.get('passwd', None)

    if not id and not passwd:
        # return JsonResponse('请填写正确的信息',safe=True)
        messages.error(request, "输入不能为空！")
        return render(request, 'shop/index.html')

    # #正则表达式判断学号格式
    # if not re.match(r'^(201).*\d{8}$',id):
    #     messages.error(request,'学 号 有 误')
    #     return render(request,'shop/index.html')

    from .models import STUDB

    users = STUDB.objects.filter(userid=id, passwd=passwd)

    if len(users) == 1:
        # 将uerid存入session方便验证
        request.session['userid'] = id
        request.session['is_login'] = '1'
        STUDB = STUDB.objects.filter(Q(userid=id, passwd=passwd)).last()
        messages.success(request, '登录成功(｡･ω･｡)ﾉ♡')
        url = 'shop/Level' + str(STUDB.rank) + '.html'
        # flag = {Encryption(id,10)}
        return render(request, url)
    else:
        messages.error(request, "啊哦~登录失败了←_←")
        return render(request, 'shop/index.html')


def jump_register(request):
    return redirect('/shop/register/')


def register(request):
    return render(request, 'shop/register.html')


def jump_login(request):
    return redirect('/shop/login/')


# 将数据存到db
def register_to_db(request):
    userid = request.POST.get('userid', None)
    username = request.POST.get('username', None)
    passwd = request.POST.get('passwd', None)
    repasswd = request.POST.get('repasswd', None)

    # 引入STUDB模板
    from .models import STUDB

    # 判断数据库内是否已经注册该学号
    users = STUDB.objects.filter(userid=userid)
    if len(users) == 1:
        messages.error(request, "这个学号已被注册！请不要试图顶替别人(｡•ˇ‸ˇ•｡)")
        return render(request, 'shop/register.html')

    # 判断学号格式
    if not re.match(r'^(201).*\d{8}$', userid):
        messages.error(request, '学 号 格 式 有 误')
        return render(request, 'shop/register.html')

    # 判断密码是否为6-12位
    if not re.match(r'^[A-Za-z0-9]{6,18}$', passwd):
        messages.error(request, "密码需要6-18位")
        return render(request, 'shop/register.html')

    # 判断是否为空
    if not userid and not passwd and not username and not repasswd:
        messages.error(request, "不要没填完就注册啊喂！")
        return render(request, 'shop/register.html')

    # 判断两次密码是否一致
    if passwd != repasswd:
        messages.error(request, "两次密码输入不一致的说")
        return render(request, 'shop/register.html')

    # 写入数据库
    STUDBdent = STUDB.objects.create(userid=userid, username=username, passwd=passwd)
    STUDBdent.save()

    messages.error(request, "注 册 成 功")
    return render(request, 'shop/index.html')


# flag加密函数
def Encryption(school_number, rank):
    encrypted = school_number
    for i in range(1, rank):
        num = hashlib.md5()
        num.update(encrypted.encode('utf-8'))
        encrypted = num.hexdigest()
        # print(encrypted),显示每一层的密文
    # print('七层加密的学号为' + encrypted)
    return encrypted


# 装饰器
def check_login(f):
    @wraps(f)
    def inner(request, *arg, **kwargs):
        if request.session.get('is_login') == '1':
            return f(request, *arg, **kwargs)
        else:
            return redirect('/login/')
    return inner


# 利用session验证登录

# def LoginCompare(request):
#     try:
#         del request.session['userid']
#     except KeyError:
#         pass
#     return HttpResponse("你已掉线")


# 验证flag是否正确
@check_login
def CompareFlag(request):
    # LoginCompare(request)
    from .models import STUDB
    flag = request.POST.get('flag', None)
    userid = request.session['userid']
    STUDB = STUDB.objects.filter(Q(userid=userid)).last()
    # return HttpResponse(STUDB.firstflag)
    if flag == '1024冲冲冲':
        if STUDB.rank == 1:
            STUDB.rank += 1
            STUDB.save()
            return Level2(request)
        else:
            messages.error(request, "请不要试图跳关(▼ヘ▼#)")
            url = 'shop/Level' + str(STUDB.rank) + '.html'
            return render(request,url)
    elif flag == '192478653':
        # 密码暂定
        if STUDB.rank == 2:
            STUDB.rank += 1
            STUDB.save()
            return Level3(request)
        else:
            messages.error(request, "请不要试图跳关(▼ヘ▼#)")
            url = 'shop/Level' + str(STUDB.rank) + '.html'
            return render(request, url)
    elif flag == '2048':
        if STUDB.rank == 3:
            STUDB.rank += 1
            STUDB.save()
            return Level4(request)
        else:
            messages.error(request, "请不要试图跳关(▼ヘ▼#)")
            url = 'shop/Level' + str(STUDB.rank) + '.html'
            return render(request, url)
    elif flag == '9649':
        if STUDB.rank == 4:
            STUDB.rank += 1
            STUDB.save()
            return Level5(request)
        else:
            messages.error(request, "请不要试图跳关(▼ヘ▼#)")
            url = 'shop/Level' + str(STUDB.rank) + '.html'
            return render(request, url)
    elif flag == 'NO ERROR':
        if STUDB.rank == 5:
            STUDB.rank += 1
            STUDB.save()
            return Level6(request)
        else:
            messages.error(request, "请不要试图跳关(▼ヘ▼#)")
            url = 'shop/Level' + str(STUDB.rank) + '.html'
            return render(request, url)
    elif flag == 'sdltql':
        # 正常通关
        if STUDB.rank == 6:
            import django.utils.timezone as timezone
            STUDB.lastflag = timezone.now()
            STUDB.timesubtract = (STUDB.lastflag - STUDB.firstflag).total_seconds()
            STUDB.save()
            return Fake_end(request)
        else:
            messages.error(request, "请不要试图跳关(▼ヘ▼#)")
            url = 'shop/Level' + str(STUDB.rank) + '.html'
            return render(request, url)
    else:
        messages.error(request, "哎呀，错了orz")
        url = 'shop/Level' + str(STUDB.rank) + '.html'
        return render(request, url)

    # 这是一段因为why理解题目错误而不得不删除的代码：）
    # if(flag == Encryption(school_number=userid,rank=STUDB.rank)):
    #     # 仅用作测试
    #     return HttpResponse(Encryption(school_number=userid,rank=STUDB.rank))
    #     STUDB.rank += 1
    #     STUDB.save()
    #     UpdateDateNormal()
    # else:
    #     return HttpResponse(Encryption(school_number=userid,rank=STUDB.rank))


# 通关后更新时间
# def UpdateDateNormal(request):
#     userid = request.session['userid']
#     STUDB = STUDB.objects.filter(Q(userid=userid)).last()
#     if(STUDB.rank == 6):
#         # 修改lastflag
#         import django.utils.timezone as timezone
#         STUDB.lastflag = timezone.now()
#         STUDB.save()
#
#
# def UpdateDateSuper(request):
#     userid = request.session['userid']
#     STUDB = STUDB.objects.filter(Q(userid=userid)).last()
#     import django.utils.timezone as timezone
#     STUDB.superflag = timezone.now()
#     STUDB.save()
#
# def UpdateDateSpecial(request):
#     userid = request.session['userid']
#     STUDB = STUDB.objects.filter(Q(userid=userid)).last()
#     import django.utils.timezone as timezone
#     STUDB.specialflag = timezone.now()
#     STUDB.save()
def Level1(request):
    return render(request, 'shop/Level1.html')


def Level2(request):
    return render(request, 'shop/Level2.html')


def Hide_Level2(request):
    return render(request, 'shop/Hide_Level2.html')


def Level3(request):
    return render(request, 'shop/Level3.html')


def Level4(request):
    return render(request, 'shop/Level4.html')


def Level5(request):
    return render(request, 'shop/Level5.html')


def Level6(request):
    return render(request, 'shop/Level6.html')


def Level7(request):
    return render(request, 'shop/Level7.html')


def Fake_end(request):
    return render(request, 'shop/Fake_end.html')


def True_end(request):
    return render(request, 'shop/True_end.html')


@check_login
def LastGame(request):
    userid = request.session['userid']
    stu = STUDB.objects.filter(Q(userid=userid)).last()
    flag = request.POST.get('flag', None)
    if stu.rank == 6 :
        if (flag == 'happy'):
                import django.utils.timezone as timezone
                stu.superflag = timezone.now()
                # 记录最后一关通关时间
                stu.timesubtract_last=(stu.superflag-stu.firstflag).total_seconds()
                stu.rank += 1
                stu.save()
                return True_end(request)
            # 彩蛋通关

        elif flag == '666':
            # 更新superflag
                import django.utils.timezone as timezone
                stu.specialflag = timezone.now()
                # 记录彩蛋通关时间
                stu.timesubtract_suprise = (stu.firstflag - stu.specialflagflag).total_seconds()
                stu.save()
                messages.success(request, '哦吼！恭喜你发现了不得了的β时间线，这一切都是命运石之门的选择~！')
                return Level7(request)
        else:
                messages.error(request, "终局之战总是很坎坷的，请再找找flag是什么吧_(:з」∠)_")
                return Level7(request)
    else:
        messages.error(request, "请不要试图跳关(▼ヘ▼#)")
        url = 'shop/Level' + str(stu.rank) + '.html'
        return render(request, url)