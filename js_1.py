# -*- coding: utf-8 -*-
# from qiniu import Auth
# from qiniu import BucketManager
#
# access_key = 'YX6Pck4xl_IXjhy9Oay7SsTB_d_XXyCrGlnnvTX7'
# secret_key = 'DQNnoew9MuGzXV3s6BL5B5BD711IQHcEQwhtnMww'
#
# q = Auth(access_key, secret_key)
# bucket = BucketManager(q)
#
# bucket_name = 'jwtime1'
# # 前缀
# prefix = None
# # 列举条目
# limit = 500
# # 列举出除'/'的所有文件以及以'/'为分隔的所有前缀
# delimiter = None
# # 标记
# marker = None
#
# ret, eof, info = bucket.list(bucket_name, prefix, marker, limit, delimiter)
# for i in ret['items']:
#     print(i['key'])
#     ret, info = bucket.delete(bucket_name, i['key'])
# a = 1


# def say():
#     print('调用了全局方法')

# def use_logging(func):
#   print("%s is running" % func.__name__())
#   return func
# @use_logging
# def bar():
#   print('i am bar')
# bar()
class _TestResult(TestResult):
  # note: _TestResult is a pure representation of results.
  # It lacks the output and reporting ability compares to unittest._TextTestResult.

  def __init__(self, verbosity=1):
    TestResult.__init__(self)
# def use_logging1():
#   print (__name__)
# use_logging1()