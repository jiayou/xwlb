# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 18:49:47 2018

@author: https://blog.csdn.net/Fighting_No1/article/details/50927180
"""

#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import os
import jieba
import re
reload(sys)
sys.setdefaultencoding('utf-8')

#对中文文本数据集进行分词
'''注意:
        1、输入的数据集路径必须是基目录/数据集名，数据集下是类别子目录，类别下是文本
        2、停用词表被放在了程序的当前目录下
        3、停用词表是我自己整理的，可以改用别的，或者不去掉停用词
        4、分词结果只包含中文\u4e00-\u9fa5，无其他特殊符合和数字
        5、如遇编码问题，请自行百度
'''

#对文本进行分词
def segment(textpath,savepath):
    global stopwords
    content=open(textpath,'r+').read()#读取文本内容
    writer=open(savepath,'w+')
    #content=content.decode('gb2312','ignore')#将gbk编码转为unicode编码
    #content=content.encode('utf-8','ignore')#将unicode编码转为utf-8编码
    #print content  #打印文本内容
    text=jieba.cut(content)#分词,默认是精确分词
    #print "/".join(text)
    for word in text:
        #通过合并所有中文内容得到纯中文内容
        word=''.join(re.findall(u'[\u4e00-\u9fa5]+', word))#去掉不是中文的内容
        word=word.strip()
        if(len(word)!=0 and not stopwords.__contains__(word)):#去掉在停用词表中出现的内容
            #print word
            writer.write(word+"\n")
    writer.flush()
    writer.close()
    print savepath+"保存好了"

#对整个文本集进行分词
def main(dir_name,tar_name):    
    if(not os.path.exists(tar_name)):
        os.mkdir(tar_name)#不存在则新建目录
    classes=os.listdir(dir_name)#该目录下的子目录，即各个类别
    classes=[r'.'] # !!!!!!!!!-------CHANGE--XLWB--ONLY-------------!!!!!
    for c in classes:
        #print c #类别
        label=dir_name+"/"+c
        files=os.listdir(label)#获取目录下的所有文本文件
        tarLabel=tar_name+"/"+c#将文本保存在相应类别的目录下
        if(not os.path.exists(tarLabel)):
            os.mkdir(tarLabel)
        #print files
        for f in files:
            print f         #打印文件名
            textpath=label+"/"+f
            savepath=tarLabel+"/"+f
            segment(textpath,savepath)

dir_name = u"./text"#数据集路径
tar_name = u"./jieba"#保存路径
stopwords = [line.strip() for line in open('cstopword.dic').readlines() ]#读取中文停用词表
main(dir_name,tar_name)


