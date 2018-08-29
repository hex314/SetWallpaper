import random
import os
import setbg

def newimg():
    path="E:/Pictures/bingImg/"
    dirs=os.listdir(path)
    return path+str(random.sample(dirs,1)[0])

setbg.setWallpaperFromBMP(newimg())

