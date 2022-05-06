
star_time = '2022-04-29_09:48:46'
total_time = '3600'
total_case = '40'
pass_case = '21'
fail_case = '19'
pass_rate = '55'
log_message = ['123','456','678','1231312','43243223423','544545']

f=open("re2.txt",'a')
f.write('自动化测试')
f.write('\n'+'测试人员：钉钉机器人'+'\n')
f.write('\n'+'开始时间：'+star_time+'\n')
f.write('\n'+'合计耗时：'+total_time+'\n')
f.write('\n'+'测试结果: '+'共 '+total_case+'，'+'通过 '+pass_case+'，'+'失败 '+fail_case+'，'+'通过率='+pass_rate+'%'+'\n')
f.write('\n'+'************************************************************失败**********************************************')
for i in range(0,len(log_message)):
    f.write('\n'+log_message[i]+'\n')
# f.flush()
f.close()


access_key = 'gMQ_x2DD6xcBsHf7Bwn4iRGFLwLilsmiW5DG3RsI'
secret_key = 'CAvmXjwUEZm8d8h_gStjOLKqy9ssx6mSHtlcFsdf'


from urllib.parse import urljoin
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
    # print(info)
    # assert ret['key'] == key
    # assert ret['hash'] == etag(local_img)

    # img_url = 空间名称 拼接 远程图片名称
    # img_url = urljoin("http://q57wyk04l.bkt.clouddn.com", img_name)
    img_url = urljoin(space2url[space_name], img_name)
    return img_url
# res = up2qiniu(r're2.txt', "jwtime1","re2.txt")
# print (res)