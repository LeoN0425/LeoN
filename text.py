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
numstat=[0]*len(words)
for i in words:
    if i not in stat:
        stat.append(i)
        s=stat.index(i)
        numstat[s]+=1
    else:
        s=stat.index(i)
        numstat[s]+=1#将每个单词不重复地放入列表中，并统计出现次数
nummax=[]
wordmax=[]
for i in range(6):
    v=numstat.index(max(numstat))
    nummax.append(numstat[v])
    wordmax.append(stat[v])
    numstat.remove(numstat[v])
    stat.remove(stat[v])#获取列表排名前六的单词与词频数

plt.bar(wordmax,nummax)
plt.title('keyword STAT')
plt.show()#用图标显示出来

arti=open(r'C:\English Test.txt')
c=arti.read()
main=tk.Tk()#创建tkinter主界面
main.geometry('1800x960')
main.title('Python文本显示')
article=tk.Message(main,text=c,width=1400)#将文本在主界面显示出来
article.config(bg='lightgreen', font=('times',14,'italic'))#设置文本参数

article.pack()