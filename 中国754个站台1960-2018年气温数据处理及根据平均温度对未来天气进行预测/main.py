# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:46:07 2020

@author: kookil
"""

from tkinter import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter.messagebox import *
from pandas import DataFrame
from tkinter import ttk
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm


def get_info():  
    location = r'754stations_infos.xlsx'
    r1=pd.read_table("max.txt",sep="\s+")
    r2=pd.read_table("min.txt",sep="\s+")
    r3=pd.read_table("平均.txt",sep="\s+")
    st_list=[]
    s1=comvalue1.get()
    s2=comvalue2.get()
    s3=comvalue3.get()
    if s1=='' and s2=='' and s3=='':
        showinfo('提醒','请至少选择一个站台')
    if s1==s2 or s1==s3 or s2==s3:
        showinfo('提醒','请选择不同的站台')
    else:
        df = pd.read_excel(location, 0)
        num1=df[df['站名']==s1]
        a1=num1['序号']
        k1=a1.values
        num2=df[df['站名']==s2]
        a2=num2['序号']
        k2=a2.values
        s3=df[df['站名']==s3]
        a3=s3['序号']
        k3=a3.values
        k_list=np.r_[k1,k2,k3]
        for k in k_list:
            st_name='st'+str(k)
            st_list.append(st_name)
        df1=DataFrame(r1[st_list])
        df2=DataFrame(r2[st_list])
        df3=DataFrame(r3[st_list])
        dff=pd.concat([df1,df2,df3],axis=1,ignore_index=True)
        return dff
    
def get_zt():
    top = Tk()
    sb = Scrollbar(top)
    sb.pack(side = RIGHT, fill = Y)
    zt= pd.read_excel('754stations_infos.xlsx')
    zt=zt.values
    
    mylist = Listbox(top, yscrollcommand = sb.set )
    for i in range(754):
        mylist.insert(END,zt[i:i+1])
    
    mylist.pack( side = LEFT )
    sb.config( command = mylist.yview )
    
    root.mainloop()
    
        
def cal_info():    
    if r.get()=="月平均日最高温度":
        m_max()
    if r.get()=="月平均日最低温度":
        m_min()
    if r.get()=="月平均日平均温度":
        m_avr()
    if r.get()=="年平均日最高温度":
        y_max()
    if r.get()=="年平均日最低温度":
        y_min()
    if r.get()=="年平均日平均温度":
        y_avr()
        
def y_min():
    dff=get_info()
    l=[]
    s=[]
    for i in range(len(dff.index.values)):
        l.append(dff.index.values[i][0])
    for j in range(int(dff.shape[1]/3)):
          r1=DataFrame(dff[1+j*3]) 
          r1['年份']=l
          d_m=r1.groupby('年份').min()
          x_value=d_m[1+j*3].index
          y_value=d_m[1+j*3].values
          s.append(y_value)
    pic(x_value,s)
    
def y_max():
    dff=get_info()
    l=[]
    s=[]
    for i in range(len(dff.index.values)):
        l.append(dff.index.values[i][0])
    for j in range(int(dff.shape[1]/3)):
          r1=DataFrame(dff[0+j*3]) 
          r1['年份']=l
          d_m=r1.groupby('年份').max()
          x_value=d_m[0+j*3].index
          y_value=d_m[0+j*3].values
          s.append(y_value)
    pic(x_value,s)

   


def y_avr():
    dff=get_info()
    l=[]
    s=[]
    for i in range(len(dff.index.values)):
        l.append(dff.index.values[i][0])
    for j in range(int(dff.shape[1]/3)):
          r1=DataFrame(dff[2+j*3]) 
          r1['年份']=l
          d_m=r1.groupby('年份').mean()
          x_value=d_m[2+j*3].index
          y_value=d_m[2+j*3].values
          s.append(y_value)
    pic(x_value,s)
    
    
def m_max():
    dff=get_info()
    l=[]
    s=[]
    for i in range(len(dff.index.values)):
        l.append(dff.index.values[i][1])
    for j in range(int(dff.shape[1]/3)):
          r1=DataFrame(dff[0+j*3]) 
          r1['月份']=l
          d_m=r1.groupby('月份').max()
          x_value=d_m[0+j*3].index
          y_value=d_m[0+j*3].values
          s.append(y_value)
    pic(x_value,s)
    
    
def m_min():
    dff=get_info()
    l=[]
    s=[]
    for i in range(len(dff.index.values)):
        l.append(dff.index.values[i][1])
    for j in range(int(dff.shape[1]/3)):
          r1=DataFrame(dff[1+j*3]) 
          r1['月份']=l
          d_m=r1.groupby('月份').min()
          x_value=d_m[1+j*3].index
          y_value=d_m[1+j*3].values
          s.append(y_value)
    pic(x_value,s)
    
    
def m_avr():
    dff=get_info()
    l=[]
    s=[]
    for i in range(len(dff.index.values)):
        l.append(dff.index.values[i][1])
    for j in range(int(dff.shape[1]/3)):
          r1=DataFrame(dff[2+j*3]) 
          r1['月份']=l
          d_m=r1.groupby('月份').mean()
          x_value=d_m[2+j*3].index
          y_value=d_m[2+j*3].values
          s.append(y_value)
    pic(x_value,s)


def pic(x,y): 
    plt.title("")
    if len(x)==12:
        plt.xlabel("月份/月")
    else:
        plt.xlabel("年份/年")   
    plt.ylabel("温度/℃")
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams["font.sans-serif"]=["SimHei"]
    if len(y)==1:
        plt.plot(x,y[0])
        plt.legend(comvalue1.get())
    elif len(y)==2:
        plt.plot(x,y[0])
        plt.plot(x,y[1])
        plt.legend([comvalue1.get(), comvalue2.get()])
    else:
        plt.plot(x,y[0])
        plt.plot(x,y[1])
        plt.plot(x,y[2])
        plt.legend([comvalue1.get(), comvalue2.get(),comvalue3.get()])
    plt.grid()
    plt.show()

def yc():
    dff=get_info()
    dff=DataFrame(dff[2])
    Enum=E1.get()
    if Enum=='':
        showinfo("警告","请确保年份的输入！")
    l=[]
    for i in range (len(dff.index)):
        s=dff.index[i][0]
        l.append(s)
    dff['年份']=l
    y_yc1=dff.groupby("年份").mean()
    plt.title("mean")
    plt.rcParams['axes.unicode_minus'] = False
    plt.rcParams["font.sans-serif"]=["SimHei"]
    plt.scatter(y_yc1.index,y_yc1.values, c='black')
    plt.xlabel("年份")
    plt.ylabel("温度")
    X = y_yc1.index.values.reshape(-1,1)
    y =y_yc1.values.reshape(-1,1)
    reg = LinearRegression()
    reg.fit(X, y)
    print("平均气温线性回归方程是: Y = {:.5} + {:.5}X".format(reg.intercept_[0], reg.coef_[0][0]))
    Enum_r=reg.intercept_[0]+ reg.coef_[0][0]*int(Enum)
    print("{}年温度约等于{}度".format(int(Enum),int(Enum_r)))
    predictions = reg.predict(X)
    plt.plot(y_yc1.index, predictions, c='blue', linewidth=2)
    plt.show()
    
def about_call():
    showinfo('帮助','1.月平均指横轴为月份，年平均指横轴为年份。2.每次选择完数据之后需要点击获取数据')
        
root = Tk()
root.title("中国754个站台1960-2018年气温数据处理")   
lb_sm=Label(root,text="请选择1-3个站台")
lb_sm.grid(row=0,column=0,ipadx=10,ipady=10,padx=10,pady=10)

lb_z1=Label(root,text="站台1")
lb_z1.grid(row=1,column=0,ipadx=10,ipady=10,padx=10,pady=10)

lb_z2=Label(root,text="站台2")
lb_z2.grid(row=2,column=0,ipadx=10,ipady=10,padx=10,pady=10)

lb_z3=Label(root,text="站台3")
lb_z3.grid(row=3,column=0,ipadx=10,ipady=10,padx=10,pady=10)

location = r'754stations_infos.xlsx'
df = pd.read_excel(location, 0)
subset = df['站名']
tuples = subset.values.tolist()

comvalue1=StringVar()
comboxlist1=ttk.Combobox(root,textvariable=comvalue1)
comboxlist1["values"]=tuples
comboxlist1.grid(row=1,column=1,ipadx=10,ipady=10,padx=10,pady=10)
comvalue2=StringVar()
comboxlist2=ttk.Combobox(root,textvariable=comvalue2)
comboxlist2["values"]=tuples
comboxlist2.grid(row=2,column=1,ipadx=10,ipady=10,padx=10,pady=10)
comvalue3=StringVar()
comboxlist3=ttk.Combobox(root,textvariable=comvalue3)
comboxlist3["values"]=tuples
comboxlist3.grid(row=3,column=1,ipadx=10,ipady=10,padx=10,pady=10)

btn_zt=Button(root,text="查看站台数据",width=20,command=get_zt)
btn_zt.grid(row=0,column=1,ipadx=10,ipady=10,padx=10,pady=10)

r=StringVar()
radio1 = Radiobutton(root, text="月平均日最高温度", variable=r,value="月平均日最高温度" )
radio1.grid(row=5,column=0,ipadx=10,ipady=10,padx=10,pady=10)
radio2 = Radiobutton(root, text="月平均日最低温度",  variable=r,value="月平均日最低温度")
radio2.grid(row=5,column=1,ipadx=10,ipady=10,padx=10,pady=10)
radio3 = Radiobutton(root, text="月平均日平均温度", variable=r,value="月平均日平均温度")
radio3.grid(row=6,column=0,ipadx=10,ipady=10,padx=10,pady=10)
radio4 = Radiobutton(root, text="年平均日最高温度",variable=r,value="年平均日最高温度")
radio4.grid(row=6,column=1,ipadx=10,ipady=10,padx=10,pady=10)
radio5 = Radiobutton(root, text="年平均日最低温度",variable=r,value="年平均日最低温度")
radio5.grid(row=7,column=0,ipadx=10,ipady=10,padx=10,pady=10)
radio6 = Radiobutton(root, text="年平均日平均温度", variable=r,value="年平均日平均温度")
radio6.grid(row=7,column=1,ipadx=10,ipady=10,padx=10,pady=10)
r.set("月平均日最高温度")

btn_pic=Button(root,text="获取数据",width=20,command=get_info)
btn_pic.grid(row=8,column=0,ipadx=10,ipady=10,padx=10,pady=10)
btn_pic=Button(root,text="作图",width=20,command=cal_info)
btn_pic.grid(row=8,column=1,ipadx=10,ipady=10,padx=10,pady=10)

lb_yc=Label(root,text="请选择1个站台的数据进行平均气温的预测")
lb_yc.grid(row=10,column=0,ipadx=10,ipady=10,padx=10,pady=10)
lb_yc=Label(root,text="请输入预测年份")
lb_yc.grid(row=11,column=0,ipadx=10,ipady=10,padx=10,pady=10)

E1 = Entry(root)
E1.grid(row=11,column=1,ipadx=10,ipady=10,padx=10,pady=10)

btn_cle=Button(root,text="清除界面",width=20,command=(lambda x=ALL: cv.delete(x)))
btn_cle.grid(row=12,column=1,ipadx=10,ipady=10,padx=10,pady=10)
btn_yc=Button(root,text="开始预测",width=20,command=yc)
btn_yc.grid(row=12,column=0,ipadx=10,ipady=10,padx=10,pady=10)

menu_bar = Menu(root)
root.config(menu=menu_bar)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About",command=about_call)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.mainloop()
