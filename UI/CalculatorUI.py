# -*- coding: utf-8 -*-
# @Time : 2022/4/14 15:34
# @Author : yyfnb
# @FileName: new calculator UI.py
from tkinter import *
import math

exp_str = ""
History_list = []
#设置窗口对象
window=Tk()
window.title('counting machine')
window.geometry("420x280")
window['bg']='black'

# 建立标签框以及标签
frame=LabelFrame(window,bg = 'white',width = 420,height = 80)
frame.pack()
frame.place(x=0,y=0)
label=Label(frame,text="",height= 3 , width=70,bg='white')
label.pack() #显示框

# 设置全局变量，即按一个button，将按钮对应的运算符加入字符串中，最后利用eval函数进行计算
global s,list,list1
s = ""
list = []
list1 = []
# 按钮0-9以及小数点的实现
#按钮.
def figure_dot():
    global s
    s=s+"."
    label.config(text=s)
btnzero=Button(window,text=".",width=4,command=figure_dot,bg='white')
btnzero.place(x=10,y=230) #按钮.

#按钮0
def figure_0():
    global s
    s=s+"0"
    label.config(text=s)
btn0=Button(window,text="0",width=4,command=figure_0,bg='white')
btn0.place(x=80,y=230) #按钮0

#按钮1
def figure_1():
    global s
    s=s+"1"
    label.config(text=s)
btn1=Button(window,text="1",width=4,command=figure_1,bg='white')
btn1.place(x=10,y=80) #按钮1

#按钮2
def figure_2():
    global s
    s=s+"2"
    label.config(text=s)
btn2=Button(window,text="2",width=4,command=figure_2,bg='white')
btn2.place(x=80,y=80)#按钮2

#按钮3
def figure_3():
    global s
    s=s+"3"
    label.config(text=s)
btn3=Button(window,text="3",width=4,command=figure_3,bg='white')
btn3.place(x=150,y=80)#按钮3

#按钮4
def figure_4():
    global s
    s=s+"4"
    label.config(text=s)
btn4=Button(window,text="4",width=4,command=figure_4,bg='white')
btn4.place(x=10,y=130)#按钮4

#按钮5
def figure_5():
    global s
    s=s+"5"
    label.config(text=s)
btn5=Button(window,text="5",width=4,command=figure_5,bg='white')
btn5.place(x=80,y=130)#按钮5

#按钮6
def figure_6():
    global s
    s=s+"6"
    label.config(text=s)
btn6=Button(window,text="6",width=4,command=figure_6,bg='white')
btn6.place(x=150,y=130)#按钮6

#按钮7
def figure_7():
    global s
    s=s+"7"
    label.config(text=s)
btn7=Button(window,text="7",width=4,command=figure_7,bg='white')
btn7.place(x=10,y=180)#按钮7

#按钮8
def figure_8():
    global s
    s=s+"8"
    label.config(text=s)
btn8=Button(window,text="8",width=4,command=figure_8,bg='white')
btn8.place(x=80,y=180)#按钮8

#按钮9
def figure_9():
    global s
    s=s+"9"
    label.config(text=s)
btn9=Button(window,text="9",width=4,command=figure_9,bg='white')
btn9.place(x=150,y=180)#按钮9


# 运算符号实现
def figure_addition():
    global s
    s=s+" + "
    label.config(text=s)
btn_add=Button(window,text="+",width=4,command=figure_addition,bg='yellow')
btn_add.place(x=220,y=80)#加法按钮

#减法按钮
def figure_subtraction():
    global s
    s=s+" - "
    label.config(text=s)
btn_sub=Button(window,text="-",width=4,command=figure_subtraction,bg='yellow')
btn_sub.place(x=220,y=130)#减法按钮

#乘法按钮
def figure_multiplication():
    global s
    s=s+" * "
    label.config(text=s)
btn_multi=Button(window,text="*",width=4,command=figure_multiplication,bg='yellow')
btn_multi.place(x=290,y=80)#乘法按钮

#除法按钮
def figure_division():
    global s
    s=s+" / "
    label.config(text=s)
btn_divi=Button(window,text="/",width=4,command=figure_division,bg='yellow')
btn_divi.place(x=290,y=130)#除法按钮

# 三角函数运算
def figure_trigonometricsin():
    global s
    s = s+" sin "
    label.config(text=s)

btn_sin=Button(window,text="sin",width=4,command=figure_trigonometricsin,bg='yellow')
btn_sin.place(x=360,y=80)#sin按钮

def figure_trigonometriccos():
    global s
    s = s + ' cos '
    label.config(text=s)

btn_cos=Button(window,text="cos",width=4,command=figure_trigonometriccos,bg='yellow')
btn_cos.place(x=360,y=130)#cos按钮

def figure_trigonometrictan():
    global s
    s = s + ' tan '
    label.config(text=s)

btn_tan=Button(window,text="tan",width=4,command=figure_trigonometrictan,bg='yellow')
btn_tan.place(x=360,y=180)#tan按钮

def figure_trigonometricarcsin():
    global s
    s = s + ' arcsin '
    label.config(text=s)

btn_arcsin=Button(window,text="arcsin",width=4,command=figure_trigonometricarcsin,bg='yellow')
btn_arcsin.place(x=220,y=180)#arcsin按钮

def figure_trigonometricarccos():
    global s
    s = s + ' arccos '
    label.config(text=s)

btn_arccos=Button(window,text="arccos",width=4,command=figure_trigonometricarccos,bg='yellow')
btn_arccos.place(x=290,y=180)#arccos按钮

def figure_trigonometricarctan():
    global s
    s = s + ' arctan '
    label.config(text=s)

btn_arctan=Button(window,text="arctan",width=4,command=figure_trigonometricarctan,bg='yellow')
btn_arctan.place(x=220,y=230)#arctan按钮

# 清空窗口button C 的实现
def figure_clear():
    global s,list,list1
    s=""
    list = []
    list1 = []
    label.config(text=s)
btn_clear=Button(window,text="clear",width=4,command=figure_clear,bg='yellow')
btn_clear.place(x=290,y=230)#清空按钮

# 结果输出函数eval
def figure_value():
    global s
    global list
    list = s.split()
    print(list)
    for i in range(len(list) ):
        if list[i] == 'sin':
            # list1.append(math.sin(math.pi/180*int(list[i+1])))
            list[i+1] = math.sin(math.pi/180*int(list[i+1]))

            # list.insert(i+1,math.sin(math.pi/180*int(list[i+1])))
            # print(math.pi/180*int(list[i+2]))
            # print(math.sin(math.pi/180*int(list[i+2])))
            # list.remove(list[i])
            # list.remove(list[i+1])

        elif list[i] == 'cos':
            # list[i+1].replace(math.cos(list[i+1]*180/math.pi))
            # del list[i]
            list[i + 1] = math.cos(math.pi / 180 * int(list[i + 1]))
        elif list[i] == 'tan':
            # list[i+1].replace(math.tan(list[i+1]*180/math.pi))
            # del list[i]
            list[i + 1] = math.tan(math.pi / 180 * int(list[i + 1]))
        elif list[i] == 'arcsin':
            # list[i+1].replace(math.asin(list[i+1]))
            # del list[i]
            list[i + 1] =int( (math.asin(float(list[i + 1])))*180/(math.pi))#将math算出的反三角函数值转化为角度
        elif list[i] == 'arccos':
            # list[i+1].replace(math.acos(list[i+1]))
            # del list[i]
            list[i + 1] = int((math.acos(float(list[i + 1])))*180/(math.pi))
        elif list[i] == 'arctan':
            # list[i+1].replace(math.atan(list[i+1]))
            # del list[i]
            list[i + 1] = int((math.atan(float(list[i + 1])))*180/(math.pi))
        else :
            # if list[i - 2] != 'sin' or list[i -1] != 'cos' or list[i -1] != 'tan' or list[i -1] != 'arcsin' or list[i -1] != 'arccos' or list[i -1] != 'arctan' :
                list1.append(list[i])
            # else :
            #     pass

    s = " ".join('%s' %id for id in list1)

    print(s)
    x=eval(s)
    s=str(x)
    label.config(text=s)

btn_value=Button(window,text="=",width=4,command=figure_value,bg='yellow')
btn_value.place(x=360,y=230)#结果按钮

window.mainloop()
