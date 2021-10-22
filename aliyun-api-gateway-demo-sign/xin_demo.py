import os
from aliyunsdkgw import client
from aliyunsdkgw.http import request
from aliyunsdkgw.common import constant

host = 'http://staging.xin.riskstorm.com'
keys = {
    'app_key': os.environ.get('ACCESS_KEY_ID', '你自己的APP_KEY'),
    'app_secret': os.environ.get('ACCESS_KEY_SECRECT', '你自己的APP_SERCET')}


def call_api(headers, url, method='GET', time_out=30000):
    cli = client.DefaultClient(**keys)
    req = request.Request(host=host, protocol=constant.HTTP, headers=headers, url=url, method=method, time_out=time_out)
    res = cli.execute(req)
    status, _, body = res
    if 200 == status or 201 == status:
        print(body.decode("utf-8"))
    else:
        print(res)


def call_risks():
    headers = {'X-Token': os.environ.get('X-Token')}
    url = '/company/91120116569319294C/risks'
    call_api(headers, url)


def call_object_names():
    headers = {'X-Token': os.environ.get('X-Token')}
    url = '/system/constants/object_names'
    call_api(headers, url)


if __name__ == '__main__':
    call_object_names()
    call_risks()
