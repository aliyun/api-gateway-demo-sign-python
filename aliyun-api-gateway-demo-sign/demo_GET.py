# -*- coding: utf-8 -*-
import os
from com.aliyun.api.gateway.sdk import client
from com.aliyun.api.gateway.sdk.http import request
from com.aliyun.api.gateway.sdk.common import constant

host = 'http://sms.market.alicloudapi.com'
uri = '/singleSendSms?'
SMS_KEYS = {
    'app_key': os.environ.get('app_key', '你自己的APP_KEY'),
    'app_secret': os.environ.get('app_secret', '你自己的APP_SERCET')}
cli = client.DefaultClient(**SMS_KEYS)

name, sid, op, sn, phone = 'xx先生', '120526', '修改密码', '1234', '18620610611,18620610612'
query = {
    'ParamString': '{{"name":"{name}","sid":"{sid}","op":"{op}","sn":"{sn}"}}'.format(**locals()),
    'RecNum': phone,
    'TemplateCode': 'SMS_67670312',
    'SignName': '公信刻'}
url = uri + '&'.join(['{}={}'.format(k, v) for k, v in query.items()])
req = request.Request(host=host,protocol=constant.HTTP, url=url, method='GET', time_out=30000)
print(cli.execute(req))

