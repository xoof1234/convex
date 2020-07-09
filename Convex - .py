#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import random
import math 
import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)
from matplotlib.figure import Figure
import time
# In[2]:

def show():
    N = int(Inputwindow.get())
    def leftMin(Point):
        minn = 0
        N = len(Point)
        for i in range(N):
            if Point[i][1] < Point[minn][1]:
                minn = i
            elif Point[i][1] == Point[minn][1]:
                if(Point[i][0] < Point[minn][0]):
                    minn = i
        return minn


    # In[3]:


    #逆時針
    def orientiation(p1,p2,p3):
        var = (p2[1]-p1[1])*(p3[0]-p2[0]) - (p3[1]-p2[1])*(p2[0]-p1[0])
        if var == 0:
            return 0
        elif var >0:
            return 1
        else:
            return 2
        


    # In[4]:


    def distance(p1,p2):
        return math.sqrt((p2[1]-p1[1])**2 + (p2[0] - p1[0])**2)


    # In[5]:


    # p0 為原點
    def angle(p1,p0):
        if(p1[0] == p0[0]):
            return 90
        elif (p1[1] == p0[1]):
            if (p1[0] - p0[1]) >0:
                return 180
            else:
                return 0
        else:
            angle = math.acos((p1[0]-p0[0])/distance(p0,p1) )
            return math.degrees(angle)


    # In[6]:


    def compare_angle(p,leftMin):
        angle_list = []
        for i in range(len(p)):
            if(i  == leftMin ):
                angle_list.append(0)
            else:
                angle_list.append(angle(p[i],p[leftMin]))
        return angle_list


    # In[21]:


    x = []
    y = []
    point = []
    for i  in range (N):
        x.append(random.randint(0,1000))
        y.append(random.randint(0,1000))
    P = list(zip(x,y))
    #find the min num
    l = leftMin(P)
    list_angle = compare_angle(P,l)
    print(list_angle)
    sort = []*100
    for i in range(N):
        count = 0
        same = []
        for j in range(N):
            if(list_angle[j] == min(list_angle)):
                same.append(j)
                count = count + 1
        if (count > 1):
            temp = []
            for j in range(count):
                temp.append(distance(P[l],P[same[j]]))
            for j in range(count):
                if(temp[j] == min(temp)):
                    sort.append(P[same[j]])
                    list_angle[same[j]] = 360
                    
        else:
            sort.append(P[same[0]])
            list_angle[same[0]] = 360      
    print(sort)
    line = [0,1]
    top = 0
    for i in range(2,N):
        var = orientiation(sort[line[top]],sort[line[top+1]],sort[i])
        if var == 2:
            line.append(i)
            top = top+1
        else:
            if (top>0):
                line.pop()
                top = top-1
                while True:
                    var = orientiation(sort[line[top]],sort[line[top+1]],sort[i])
                    if var == 2:
                        line.append(i)
                        top = top+1
                        break
                    else:
                        line.pop()
                        top = top-1
                        if(top<0):
                            break
    f = Figure(figsize=(5,4),dpi = 100)
    a = f.add_subplot(111)
    canvas = FigureCanvasTkAgg(f, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    for i in range(len(line)-1):
        a.scatter(x,y)
        for j in range(i+1):
            a.plot([sort[line[j]][0],sort[line[j+1]][0]],[sort[line[j]][1],sort[line[j+1]][1]])
            time.sleep(0.01)
        canvas.draw()
    a.scatter(x,y)
    for i in range(len(line)-1):
        a.plot([sort[line[i]][0],sort[line[i+1]][0]],[sort[line[i]][1],sort[line[i+1]][1]])
    a.plot([sort[line[0]][0],sort[line[-1]][0]],[sort[line[0]][1],sort[line[-1]][1]])
    canvas.draw()

# In[ ]:

window = tk.Tk()
label = tk.Label(window,text = "number")

var = tk.StringVar()
Inputwindow = tk.Entry(window,textvariable = var)
Inputwindow.pack()

resultBtn = tk.Button(window,text = 'Result',command = show)
resultBtn.pack()

window.mainloop()
