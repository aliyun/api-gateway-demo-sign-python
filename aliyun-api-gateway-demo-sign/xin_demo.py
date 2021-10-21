# -*- coding: utf-8 -*-
import os
from com.aliyun.api.gateway.sdk import client
from com.aliyun.api.gateway.sdk.http import request
from com.aliyun.api.gateway.sdk.common import constant


def call_api():
    host = 'http://staging.xin.riskstorm.com'
    url = '/company/91120116569319294C/risks'
    keys = {
        'app_key': os.environ.get('ACCESS_KEY_ID', '你自己的APP_KEY'),
        'app_secret': os.environ.get('ACCESS_KEY_SECRECT', '你自己的APP_SERCET')}
    cli = client.DefaultClient(**keys)
    headers = {'X-Token': os.environ.get('X-Token')}
    req = request.Request(host=host, protocol=constant.HTTP, headers=headers, url=url, method='GET', time_out=30000)
    res = cli.execute(req)
    print(res)
    status, headers, body = res
    print(body.decode("utf-8"))


if __name__ == '__main__':
    call_api()
