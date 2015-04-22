#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib
import hashlib
import urllib
import urllib2
import sys
sys.path.append("..")


def md5(str):
    import hashlib
    import types
    if isinstance(str, types.StringType):
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''


def capture(str):
    pass


def getCookie():
    import common
    import re
    dic = {'cmd': 'loginCorp', 'cacct': 'xndian',
           'sacct': common.UNAME, 'pwd': md5(common.PWD)}
    params = urllib.urlencode(dic)
    req = urllib2.Request(url=common.LOGIN_URL, data=params)
    res_data = urllib2.urlopen(req).read()
    if 'true' in res_data:
        sh = re.findall(r'sessionId.*?}', res_data)[0]
        return sh.replace('sessionId":"', '').replace('"}', '')
    else:
        return 'error'
