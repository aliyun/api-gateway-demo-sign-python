### 1、本示例的 Python 版本为3.9
- 参考官方已经过期的aliyun gw demo（python 2.7）
https://github.com/aliyun/api-gateway-demo-sign-python?spm=5176.14097614.0.0.3d714afbTA4B0O 
- 参考官方已经过期的aliyun gw demo（python 3.6）
https://github.com/williezh/api-gateway-demo-sign-python/
- 从3.6支持迁移到3.9，解决3.9迁移兼容问题，修复header透传问题，调整原来文件结构和命名方式

### 2、本demo主要是为了提供签名方法，调用示例可以参考 demo.py 文件

### 3、使用注意事项：
- 含有中文和空格的query, body在请求时需要对值进行urlencode处理，编码为utf-8.
- 参数参与签名时，必须使用原文签名，不能用urlencode后字符串的进行签名.所以请在签名之后再对query、body的值做urlencode.
- [签名文档](https://help.aliyun.com/document_detail/29475.html)
