import base64
import hmac
import hashlib
import urllib
h = hmac.new('LTAI5tFSTHaPyqhsutxPFWz8',
             "GET\n\n\n1141889120\n%2Fexamplebucket%2Foss-api.pdf?\
             &x-oss-ac-forward-allow=true\
             &x-oss-ac-source-ip=127.0.0.1\
             &x-oss-ac-subnet-mask=32\
             &x-oss-signature-version=OSS2",
             hashlib.sha256)
Signature = base64.encodestring(h.digest()).strip()