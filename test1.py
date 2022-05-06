# -*- coding: utf-8 -*-
"""
Python SDK_SDK_对象存储 - 七牛开发者中心
https://developer.qiniu.com/kodo/sdk/1242/python#3

"""

# from qiniu import Auth, put_file, etag
# import qiniu.config
#
# #需要填写你的 Access Key 和 Secret Key
# access_key = 'YX6Pck4xl_IXjhy9Oay7SsTB_d_XXyCrGlnnvTX7'
# secret_key = 'DQNnoew9MuGzXV3s6BL5B5BD711IQHcEQwhtnMww'
#
# #构建鉴权对象
# q = Auth(access_key, secret_key)
#
# #要上传的空间
# bucket_name = 'jwtime'
#
# #上传后保存的文件名
# key = 'testupimg.png'
#
# #生成上传 Token，可以指定过期时间等
# token = q.upload_token(bucket_name, key, 3600)
#
# #要上传文件的本地路径
# localfile = r'D:\jw8\a.png'
#
# ret, info = put_file(token, key, localfile)
# print(info)
# assert ret['key'] == key
# assert ret['hash'] == etag(localfile)


"""
Python SDK_SDK_对象存储 - 七牛开发者中心
https://developer.qiniu.com/kodo/sdk/1242/python#3

"""

# 需要填写你的 Access Key 和 Secret Key
access_key = 'gMQ_x2DD6xcBsHf7Bwn4iRGFLwLilsmiW5DG3RsI'
secret_key = 'CAvmXjwUEZm8d8h_gStjOLKqy9ssx6mSHtlcFsdf'


from urllib.parse import urljoin


# 目标
# 写一个函数，功能是上传本地图片
# 返回值是上传后的网络图片的地址

# 空间名称与空间网址的对应字典
space2url ={
    "jwtime1":"http://tangjw.xyz",
    "x":"123"
}

def up2qiniu(local_img,space_name,img_name):
    """
    本图图片的上传
    :param local_img: 本地图片路径
    :param space_name: 云服务器的空间名称
    :param img_name: 上传后的网络上保存的图片名称
    :return img_url: 远程图片的路径(绝对路径)
    """

    from qiniu import Auth, put_file, etag
    import qiniu.config

    access_key = 'YX6Pck4xl_IXjhy9Oay7SsTB_d_XXyCrGlnnvTX7'
    secret_key = 'DQNnoew9MuGzXV3s6BL5B5BD711IQHcEQwhtnMww'

    # 构建鉴权对象
    q = Auth(access_key, secret_key)

    # 要上传的空间
    bucket_name = 'jwtime1'

    # 上传后保存的文件名
    key = img_name

    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)

    # 要上传文件的本地路径
    # localfile = r'D:\jw8'

    ret, info = put_file(token, key, local_img)
    print(info)
    # assert ret['key'] == key
    # assert ret['hash'] == etag(local_img)

    # img_url = 空间名称 拼接 远程图片名称
    # img_url = urljoin("http://q57wyk04l.bkt.clouddn.com", img_name)
    img_url = urljoin(space2url[space_name], img_name)
    return img_url

res = up2qiniu(r'c.png', "jwtime1","c.png")
print(res)


