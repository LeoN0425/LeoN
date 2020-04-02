import matplotlib.pyplot as plt
import tkinter as tk

art=open(r'C:\English Test.txt')#读取文件
punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~…0123456789'#标点符号 
readline=art.readlines()
words=[]
for line in readline:
    line=line.strip()#去除首尾空格
    for i in line:
        if i in punctuation:
            line=line.replace(i,' ')#讲标点符号替换为空格
    word=line.split(' ')#以空格为界划分文本
    for i in word:
        if i!='':
            words.append(i.lower())#去除掉所有零元素，并转化为小写
stat=[]