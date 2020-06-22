__author__ = 'wanderknight'
__time__ = '2020/2/1 12:35'

from django.db import models


class BaseModel(models.Model):
    """模型抽象基类
    :return"""
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    class Meta:
        # 说明是一个抽象模型类
        abstract = True
