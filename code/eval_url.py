# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 14:32:09 2019

@author: peter
"""
import re
def get_len(url):
    return len(url)

def get_url_count(url):
    if re.search('(http://)|(https://)', url, re.IGNORECASE) :
        return 1
    else:
        return 0

def get_evil_char(url):
    return len(re.findall("[<>,\'\"/]", url, re.IGNORECASE))

def get_evil_word(url):
    return len(re.findall(("(alert)|(script=)(%3c)|(%3e)"
        "|(%20)|(onerror)|(onload)|(eval)|(src=)|(prompt)"),url,re.IGNORECASE))


def get_feature(url):
    return [get_len(url),get_evil_char(url),get_evil_word(url)]

