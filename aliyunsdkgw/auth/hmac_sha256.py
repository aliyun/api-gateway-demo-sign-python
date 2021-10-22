# -*- coding:utf-8 -*-
#  Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# coding=utf-8


import hmac
import hashlib
import base64


class six:  # or `pip install six` and `import six`
    import sys
    text_type = str if sys.version_info[0] == 3 else unicode
    binary_type = bytes if sys.version_info[0] == 3 else str


def ensure_binary(value):
    if isinstance(value, six.text_type):
        value = value.encode(encoding='utf-8')
    return value


def ensure_str(value):
    if isinstance(value, six.binary_type):
        value = value.decode(encoding='utf-8')
    return value


def sign(source, secret):
    h = hmac.new(ensure_binary(secret), ensure_binary(source), hashlib.sha256)
    signature = base64.encodebytes(h.digest()).strip()
    return ensure_str(signature)

