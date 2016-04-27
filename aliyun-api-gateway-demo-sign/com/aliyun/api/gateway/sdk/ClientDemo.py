from com.aliyun.api.gateway.sdk import client
from com.aliyun.api.gateway.sdk.http import request
from com.aliyun.api.gateway.sdk.common import constant

host = "http://test.ca-cn-qingdao.aliapi.com"
url = "/test/number?age=20&phone=10&postcode=-1"

# req = request.Request(host=host, url=url, method="GET", time_out=30000)
#
cli = client.DefaultClient(app_key="app_key", app_secret="app_secret")
#
# print cli.execute(req)



url = "/python/bytes"

import json
req_post = request.Request(host=host, url=url, method="POST", time_out=30000)
body = {}
body["name"] = "testName1111111"
body["address"] = "testAddress"
# body["email"]="testemail@123.com"
req_post.set_body(bytearray(source=json.dumps(body), encoding="utf8"))
req_post.set_content_type(constant.CONTENT_TYPE_STREAM)
print cli.execute(req_post)
