import requests
import win32api,win32con,win32gui
import time
import os
# 请求网页，跳转到最终 img 地址
def get_img_url(raw_img_url = "https://area.sinaapp.com/bingImg/"):
    r = requests.get(raw_img_url)       
    img_url = r.url # 得到图片文件的网址
    print('img_url:', img_url)
    return img_url
#访问图片地址
html = requests.get(get_img_url())
#将图片保存到D盘bing目录
nowtime = time.strftime("%Y.%m.%d")
if not os.path.exists("d:/bing"):
    os.mkdir("d:/bing")

#下载文件，以日期命名
with open("d:/bing/bing %s.jpg" %nowtime,"wb")as f:
    f.write(html.content)

def setWallPaper(pic_path):
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ, "2") 
    win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic_path, win32con.SPIF_SENDWININICHANGE)

setWallPaper("D:/bing/bing %s.jpg" %nowtime)

