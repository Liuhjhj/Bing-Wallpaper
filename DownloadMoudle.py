# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liuhjhj
@File           :  DownloadMoudle.py
"""
import requests
import re


def check_internet(url='about:blank'):
    head = {
        'User-Agent': 'Mozilla/5.0(Windows; U; Windows NT 6.1;'
        ' en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    Timeout = 30
    try:
        Page = requests.session().get(url, headers=head, timeout=Timeout)
        Page.encoding = 'UTF-8'
        return Page.text
    except BaseException as e:
        return 'Error'

def download_file(file, url):
    try:
        r = requests.get(url, stream=True)
        with open(file, 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)
    except Exception as e:
        return 'Error'

def download_start(n='1'):
    site = 'https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=' + n + '&nc=1563720256934&pid=hp'
    print('site=',site)
    text = check_internet(site)
    print('text=', text)
    if text == 'Error' or text == 'null':
        print('Fail')
        return 'DownloadFail'
    patterns = re.compile(r'"url":".*?"')
    istp = re.findall(patterns, text)
    return istp
