# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:34:37 2019

@author: alchemylee
"""
###################################################################################################################################3

from PIL import Image # PIL 是一个 Python 图像处理库

#ascii_char = list("▇*")
#ascii_char = list("一乙二十丁厂七卜人入八九几儿了力乃刀又三于干亏扛寺吉扣考托老执巩圾扩扫地扬场耳共芒亚芝朽朴机权过硬确雁殖裂雄暂雅辈悲紫辉敞赏掌晴暑最量")
# 是我们的字符画所使用的字符集，一共有 70 个字符，字符的种类与数量可以自己根据字符画的效果反复调试的
ascii_char = list("杨潇是个大傻逼")
WIDTH = 300 # 字符画的宽
HEIGHT = 300 # 字符画的高


# 将256灰度映射到7个字符上，也就是RGB值转字符的函数：
def get_char(r, g, b, alpha=256):  # alpha透明度
   if alpha == 0:
       return '口'
   length = len(ascii_char)
   #gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 计算灰度
   gray = int(0.3333*r+0.3333*g+0.3333*b)
   unit = (256.0 + 1) / length
   return ascii_char[int(gray / unit)]  # 不同的灰度对应着不同的字符
   # 通过灰度来区分色块


if __name__ == '__main__':
   img = 'C:/LT/python/code/IMG-字符/8.jpg' # 图片所在位置
   im = Image.open(img)
   im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
   txt = ""
   for i in range(HEIGHT):
       for j in range(WIDTH):
           txt += get_char(*im.getpixel((j, i))) # 获得相应的字符
       txt += '\n'
   print(txt)  # 打印出字符画
   # 将字符画 写入文件中
   with open("C:\LT\python\code\IMG-字符\output.txt", 'w') as f:
       f.write(txt)
###############################################################################################################################










































