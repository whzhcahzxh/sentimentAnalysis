# -*- coding: UTF-8 -*-  
'''
Created on 2013-12-12

@author: Hao
'''
# import jieba
# import pymongo
from getAccessToken import getAcc
from userSpammerDetect import detector
from filterComment import filterWeibo
# 做搜索
# seg_list = jieba.cut("我来到北京清华大学",cut_all=True)  
# print "Full Mode:", "/ ".join(seg_list) #全模式  

client = getAcc().accessToken_get()

#建立mongoDB连接
# conn = pymongo.Connection('localhost',27017)
# db = conn.test
# dbCollection = db.weibo

# 得到关注的微博
status = client.statuses.friends_timeline.get()
get_statuses = status.__getattr__('statuses')
# type(get_statuses)
#输出每一条微博以及微博的评论
for count in range(len(get_statuses)):
# for count in range(5):
    print "~~~~~~~~~一条新微博~~~~~~~~~~~~~"
    weibo = get_statuses[count]['text']
    print "weibo: " + str(weibo)
    
    messageid = get_statuses[count]['mid']
    commentCount = 0
    while True:
        comments = client.comments.show.get(id=messageid, count=200, page=commentCount/200+1)
#     seg_list = jieba.cut(comments, cut_all=False)
#     print "| ".join(seg_list) 
    
        get_comments_status = comments.__getattr__('comments')
        numberOfSpammer = 0
        numberOfReal = 0
        for i in range(len(get_comments_status)):
            comment = get_comments_status[i]['text']
            print "origin comment: "+comment
            print "comment: "+filterWeibo().filtering(comment)
            userInfo = get_comments_status[i]['user']
            result = detector().detect(userInfo)
            if result:
                print "不健康用户"
                numberOfSpammer+=1
            else:
                print "真实用户"
                numberOfReal+=1
        
        commentCount+=200
        comments.__getattr__('total_number')
        totalComment = comments['total_number']
        print str(commentCount)+"--评论数"+"    总共有："+str(totalComment)
        if commentCount>=totalComment:
            break;
#       写入mongoDB
#     dbCollection.insert({"weibo":get_statuses[count],"count":count,"comments":comments, "numberOfSpammer":numberOfSpammer, "numberOfReal":numberOfReal})
        

