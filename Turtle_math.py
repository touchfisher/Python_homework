'''
Author: 刘博文
Date: 2023-03-17 21:36:09
LastEditTime: 2023-03-18 23:40:54
FilePath: Turtle_math.py
Description: 
https://github.com/touchfisher
Copyright (c) 2023 by touchfisher, All Rights Reserved. 
'''
import turtle as t
import random

def draw_box():
    t.pendown()
    for _ in range(4):
        t.forward(30)
        t.left(90)
    t.penup()
    t.forward(30)

def generate_question(operation, num1, num2, ans):
    question = "%2d"%(num1) + operation + "%2d = "%(num2) + "%2d" %(ans)
    return question

def generate_addition_question():
    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99 - num1)
    ans = num1 + num2
    question = generate_question("+", num1, num2, ans)
    return question

def generate_subtraction_question():
    num1 = random.randint(0, 99)
    num2 = random.randint(0, num1)
    ans = num1 - num2
    question = generate_question("-", num1, num2, ans)
    return question

def generate_multiplication_question():
    num1 = random.randint(1, 99)
    num2 = random.randint(0, 99 // num1)
    ans = num1 * num2
    question = generate_question("×", num1, num2, ans)
    return question

def generate_division_question():
    num2 = random.randint(1, 99)
    num1 = num2 * random.randint(1, 99 // num2)
    ans = num1 // num2
    question = generate_question("÷", num1, num2, ans)
    return question

def generate_question_list():
    # 为了保持顺序，必须用列表类型
    question_list = []
    while len(question_list) < 15:
        operation = random.choice(["+", "-", "×", "÷"])
        if operation == "+":
            question = generate_addition_question()
        elif operation == "-":
            question = generate_subtraction_question()
        elif operation == "×":
            question = generate_multiplication_question()
        else:
            question = generate_division_question()
        if question not in question_list:
            question_list.append(question)
    return question_list

if __name__ == "__main__":
    # 设置画布大小和画笔速度
    t.setup(800,800)
    t.speed(10)

    # 移动初始位置到左上角
    t.pu()
    t.goto(-330,350)

    # 写标题
    t.write("试题",font=("宋体",16,"normal"))
    t.fd(50)
    t.pencolor('blue')
    t.write("(Quiz)",font=("宋体",16,"normal"))

    # 画标题线
    t.goto(-330,340)
    t.pencolor('black')
    t.pd()
    t.fd(650)

    question_list = generate_question_list()
    it1 = iter(question_list)
    it2 = iter(question_list)
    x,y = -320,300
    for i in range(5):
        for j in range(3):
            t.pu()
            t.goto(x,y)
            t.write(next(it1)[:-2],font=("Courier New", 16, "normal"))
            x+=100
            t.goto(x,y)
            draw_box()
            x+=150
        x = -320
        y -= 50

    # 写答案标题
    y-=50
    t.pu()
    t.goto(x,y)
    t.write("答案",font=("宋体",16,"normal"))
    t.fd(50)
    t.pencolor('blue')
    t.write("(Answer)",font=("宋体",16,"normal"))

    # 画答案标题线
    y-=10
    t.goto(x,y)
    t.pencolor('black')
    t.pd()
    t.fd(650)

    # 答案
    x=-320
    y-=40
    for i in range(5):
        for j in range(3):
            t.pu()
            t.goto(x,y)
            t.write(next(it2),font=("Courier New", 16, "normal"))
            x+=100
            t.goto(x,y)
            draw_box()
            x+=150
        x = -320
        y -= 50

    x += 550
    y -= 50
    t.pu()
    t.goto(x,y)
    t.write("刘博文\nM202221325",font=("宋体",16,"normal"))
    t.done()