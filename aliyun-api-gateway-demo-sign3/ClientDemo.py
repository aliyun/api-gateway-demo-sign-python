# -*- coding: utf-8 -*-
from com.aliyun.api.gateway.sdk import client
from com.aliyun.api.gateway.sdk.http import request
from com.aliyun.api.gateway.sdk.common import constant

host = "http://test-cn-qingdao.alicloudapi.com"
url = "/api/path"

cli = client.DefaultClient(app_key="your appKey", app_secret="your appSecret")


# demo of [HTTP GET] type request
# req = request.Request(host=host, protocol=constant.HTTP, url=url, method="GET", time_out=30000)
# print(cli.execute(req))


# demo of [HTTP POST body stream] type request
# import json
# req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="POST", time_out=30000)
# body = {"name": "testName", "address": "testAddress", "email": "testemail@123.com"}
# req_post.set_body(bytearray(source=json.dumps(body), encoding="utf8"))
# req_post.set_content_type(constant.CONTENT_TYPE_STREAM)
# print(cli.execute(req_post))


# demo of [HTTP POST form] type request
req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="POST", time_out=30000)
bodyMap = {"param1": "value1", "param2": "value2"}
req_post.set_body(bodyMap)
req_post.set_content_type(constant.CONTENT_TYPE_FORM)
print(cli.execute(req_post))


# demo of [HTTPS POST form] type request
# req_post = request.Request(host=host, protocol=constant.HTTPS, url=url, method="POST", time_out=30000)
# bodyMap = {"param1": "value1", "param2": "value2"}
# req_post.set_body(bodyMap)
# req_post.set_content_type(constant.CONTENT_TYPE_FORM)
# print(cli.execute(req_post))
