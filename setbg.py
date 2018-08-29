'''
程序功能：将指定路径的图片设置为桌面壁纸
程序原理：先将图片转为bmp格式，然后调用win系统api设置壁纸
'''

from PIL import Image
import os
import win32gui,win32con,win32api

def setWallpaperFromBMP(imgpath):
    try :
        xxx=Image.open(imgpath)
        bgg=xxx.save('tmp.bmp')
    except IOError:
        print("cannot convert")
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
        "Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2") 
    #2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, bgg, 1+2)
    os.remove('tmp.bmp')
    print(imgpath)

