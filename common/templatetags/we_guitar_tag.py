#encoding=utf-8

import time
import pytz
from django import template
from django.conf import settings


register = template.Library()


@register.filter(name='hdatetime')
def repr_datetime(value) -> str:
    if not value:
        return ''
    tz = pytz.timezone(settings.TIME_ZONE)
    return value.astimezone(tz).strftime('%Y-%m-%d %H:%M:%S')


@register.filter(name='cn_hdatetime')
def cn_hdatetime(value) -> str:
    if not value:
        return ''
    tz = pytz.timezone(settings.TIME_ZONE)
    return value.astimezone(tz).strftime('%m月%d日 %H:%M')


