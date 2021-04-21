# -*- coding: utf-8 -*-

import json

from django import template

register = template.Library()

@register.filter
def path_to_links(value):
    split_data=value.split('/')
    split_data.remove('')

    NUM=num=len(split_data)-1
    r_data=list()
    for i in range(0, NUM):
        link=''
        for j in range(0, num):
            link=f'{link}/{split_data[j]}'
        # link=f'{link}/'
        if i>0:
            r_data.append([link, split_data[j]])
        else:
            r_data.append(['', split_data[j]])
        num-=1
    r_data.append(['/', 'Home'])
    return(reversed(r_data))

@register.filter
def json_loads(value):
    return(json.loads(value))