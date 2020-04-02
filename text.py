import matplotlib.pyplot as plt
import tkinter as tk

art=open(r'C:\English Test.txt')#读取文件
punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~…0123456789'#标点符号 
readline=art.readlines()
words=[]