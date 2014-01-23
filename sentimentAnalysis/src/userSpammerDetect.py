# -*- coding: UTF-8 -*-  
'''
Created on 2013-12-13

@author: administrator
'''
class detector():
    def __init__(self):
        self.score = 0
        self.isSpammer = False
        
    def detect(self,userInfo):
        followersCount = userInfo['followers_count']
        friendsCount = userInfo['friends_count']
        domain = userInfo['domain']
        biFollowersCount = userInfo['bi_followers_count']
        statusesCount = userInfo['statuses_count']
        profileImageUrl = userInfo['profile_image_url']
        location = userInfo['location']
        description = userInfo['description']
        verified = userInfo['verified']
#         screenName = userInfo['screen_name']
        favouritesCount = userInfo['favourites_count']
        url = userInfo['url']
        
#         print "userInfo: "+ str(userInfo)
#         
#         print "粉丝数: "+ str(followersCount)
#         print "关注数: "+ str(friendsCount)
#         print "域名: "+ str(domain)
#         print "互粉数: "+str(biFollowersCount);
#         print "发微博数: "+str(statusesCount);
#         print "头像地址： "+str(profileImageUrl)
#         print "位置: "+str(location);
#         print "个人描述: "+str(description);
#         print "验证用户: "+str(verified);
#         print "用户名: "+str(screenName);
#         print "赞: "+str(favouritesCount);
#         print "个人网址: "+str(url);
        
        if verified:
            self.score += 10000
        else:
            if followersCount!=0:                
                if followersCount<=10 or friendsCount<=10 or (friendsCount-followersCount)>=500:
                    self.score-=500
                elif friendsCount/followersCount<=1:
                    self.score+=200
                elif friendsCount/followersCount<=3 and friendsCount/followersCount>1:
                    self.score+= (-200)*(friendsCount/followersCount)+400
                else:
                    self.score-=500 
            else:
                self.score-=2000
            if friendsCount>=100:
                self.score += (biFollowersCount/friendsCount)*400-200;    
            
            if str(len(domain))>0:
                self.score+=100
      
            if statusesCount<=10:
                self.score-=500

            if location=="其他":
                self.score-=200
                
            if profileImageUrl=="http://tp3.sinaimg.cn/3044566894/50/0/1" or profileImageUrl=="http://tp3.sinaimg.cn/3214471294/50/0/0":
                self.score-=200           
                
            if len(description)>=5:
                self.score+=100
            else:
                self.score-=100
                
            if favouritesCount>=10:
                self.score+=100
                
            if len(url)>0:
                self.score+=200
                
                
        if self.score>=0:
            self.isSpammer = False
        else:
            self.isSpammer = True
        return self.isSpammer
    
    