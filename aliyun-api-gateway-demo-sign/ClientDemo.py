# -*- coding: utf-8 -*-
from com.aliyun.api.gateway.sdk import client
from com.aliyun.api.gateway.sdk.http import request
from com.aliyun.api.gateway.sdk.common import constant

host = "http://test-cn-qingdao.alicloudapi.com"
url = "/api/billing/test/123243?queryparam=query1"

cli = client.DefaultClient(app_key="appKey", app_secret="appSecret")

# GET
# req = request.Request(host=host,protocol=constant.HTTP, url=url, method="GET", time_out=30000)
# print cli.execute(req)


#post body stream

# import json
# req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="POST", time_out=30000)
# body = {}
# body["name"] = "testName1111111"
# body["address"] = "testAddress"
# body["email"] = "testemail@123.com"
# req_post.set_body(bytearray(source=json.dumps(body), encoding="utf8"))
# req_post.set_content_type(constant.CONTENT_TYPE_STREAM)
# print cli.execute(req_post)


#post form

req_post = request.Request(host=host, protocol=constant.HTTP, url=url, method="POST", time_out=30000)
bodyMap = {}
bodyMap["bodyForm1"] = "fwefwef"
bodyMap["bodyForm2"] = "ffwefwef"
req_post.set_body(bodyMap)
req_post.set_content_type(constant.CONTENT_TYPE_FORM)
print cli.execute(req_post)