'''
Author: 刘博文
Date: 2023-03-17 20:57:17
LastEditTime: 2023-03-18 23:39:17
FilePath: turtle_autodraw.py
Description: 自己开发的一个可根据图片内容自动利用Turtle绘制图像的代码
https://github.com/touchfisher
Copyright (c) 2023 by touchfisher, All Rights Reserved. 
声明：以下代码均为本人独立编写
'''
from PIL import Image
import turtle as t

def draw_one_pix(pix):
    '''
    param pix: 传入包含某一个像素的信息(x,y,r,g,b)的元组，将其绘制。
    '''
    x,y,r,g,b = pix
    # 画笔抬起
    t.pu()
    # 移动到对应位置
    t.goto(x-100,-y+100)
    # 画笔落下
    t.pd()
    # 改变画笔颜色
    t.pencolor(r,g,b)
    # 画这个像素(向前移动1个像素值)
    t.fd(1)

def draw_img(img_path):
    '''
    param img_path: 利用Turtle模块绘制指定路径'img_path'下的图像。
    '''
    img = Image.open(img_path)
    # resize到一个较小尺寸，缩短绘图时间，当然这行可以去掉
    img = img.resize((224,224))
    width, height = img.size
    # 这里是因为使用pil读取图片时，默认是按bgr读取的，所以需要进行转换
    img = img.convert('RGB')
    # 使用重循环遍历图像像素，将像素信息存入pix_map中
    pix_map = []
    for j in range(width):
        for i in range(height):
            r, g, b = img.getpixel((i, j))
            index_and_rgb = (i, j, r, g, b)
            pix_map.append(index_and_rgb)

    # 设置画笔属性，255为rgb模式，tracer(False)和update()配合使用
    # 达到动态绘制效果
    t.colormode(255)
    t.tracer(False)
    
    count = 0
    for pix in pix_map:
        draw_one_pix(pix)
        count += 1
        # 每500像素更新一次绘制信息
        if count % 500 ==0:
            t.update()
    t.update()

if __name__ == "__main__":
    # 指定绘制图片的路径
    img_path = r'a.jpg'
    draw_img(img_path)
    
    # 写自己的姓名和学号
    t.color('white')
    t.write("刘博文\nM202221325", align="right",font=("宋体",10,"normal"))
    t.update()
    t.done()
    