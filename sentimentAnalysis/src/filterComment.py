# -*- coding: UTF-8 -*-  
'''
Created on 2013-12-16

@author: administrator
'''
class filterWeibo():
    @staticmethod
    def filtering(comment):
        while True:
            index = comment.find("//@")
            if index==-1:
                break;
            else:
                comment = comment[:index]
        while True:
            index = comment.find("/@")
            if index==-1:
                break;
            else:
                comment = comment[:index]
        while True:
            index = comment.find("http://t.cn")
            if index==-1:
                break;
            else:
                comment = comment[:index]+comment[index+19:]                
        while True:
            index = comment.find("#")
            if index==-1:
                break;
            else:
                index1 = comment.find("#", index+1)
                if index1==-1:
                    comment = comment[:index]+comment[index+1:]
                else:
                    index2 = comment.find("来自话题", 0,index)
                    if index2==-1:
                        comment = comment[:index]+comment[index1+1:]
                    else:
                        comment = comment[:index2]+comment[index1+1:]
        while True:
            index = comment.find("回复@")
            if index==-1:
                break;
            else:
                index1 = comment.find(":",index+1)
                if index1==-1:
                    comment = comment[:index]+comment[index+7:]
                else:
                    comment = comment[:index]+comment[index1+1:]
        while True:
            index = comment.find("@")
            if index==-1:
                break;
            else:
                index1 = comment.find(" ",index+1)
                if index1==-1:
                    comment = comment[:index]
                else:
                    comment = comment[:index]+comment[index1+1:]
        while True:
            index = comment.find("转发微博")
            if index==-1:
                break;
            else:
                comment = comment[:index]+comment[index+12:]
        while True:
            index = comment.find("[")
            if index==-1:
                break;
            else:
                index1 = comment.find("]",index+1)
                if index1==-1:
                    comment = comment[:index]+comment[index+1:]
                else:
                    comment = comment[:index]+comment[index1+1:]
    
        return comment
if __name__ == "__main__":
    print str(filterWeibo().filtering("[哈哈]"))