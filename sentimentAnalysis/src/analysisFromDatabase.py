# -*- coding: UTF-8 -*-
'''
Created on Dec 23, 2013

@author: administrator
'''
import pymongo
import jieba
from filterComment import filterWeibo

conn = pymongo.Connection('localhost',27017)
db = conn.test
dbCollection = db.database

cursor = dbCollection.find()
count=0
for commentPiece in cursor:
    sentence = commentPiece['content']
    sentence = filterWeibo.filtering(sentence)
    if "哈哈" in sentence:
        count+=1
        word = jieba.cut(sentence)
        print "|".join(word) +"    数量： "+str(count)
#         jieba.