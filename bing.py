#程序功能：抓取必应每日一图，设置为桌面壁纸

import urllib.request
import requests         
import os.path
import ctypes
import setbg

def save_img(img_url,dirname):
    #保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            print ('文件夹',dirname,'不存在，重新建立')
            #os.mkdir(dirname)
            os.makedirs(dirname)
        #获得图片文件名，包括后缀
        basename = os.path.basename(img_url)
        #拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        #下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url,filepath)
    except IOError as e:
        print ('文件操作失败',e)
    except Exception as e:
        print ('错误 ：',e)
    print("Save", filepath, "successfully!")

    return filepath

# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)       
    img_url = r.url # 得到图片文件的网址
    print('img_url:', img_url)
    return img_url

def main():
    dirname = "E:\\Pictures\\bingImg"       # 图片要被保存在的位置
    img_url = get_img_url()
    filepath = save_img(img_url, dirname)   # 图片文件的的路径
    setbg.setWallpaperFromBMP(filepath)

main()