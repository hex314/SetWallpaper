'''
程序功能：获取指定文件夹中的随机文件，将其设置为桌面壁纸
'''

import random
import os
import setbg

def newimg():
    path="E:/Pictures/bingImg/"
    dirs=os.listdir(path)
    return path+str(random.sample(dirs,1)[0])

setbg.setWallpaperFromBMP(newimg())

