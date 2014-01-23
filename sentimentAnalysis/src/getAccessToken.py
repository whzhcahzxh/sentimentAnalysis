# -*- coding: UTF-8 -*-  
'''
Created on 2013-12-13

@author: administrator
'''
from weibo import APIClient
import urllib,httplib

class getAcc():
    def __init__(self):
        print "get access token"       
    
    def accessToken_get(self):
        APP_KEY = '1690375172'
        APP_SECRET = 'e09cff8b33bd34426831fbf63caf00ca'
        CALLBACK_URL = 'http://weibo.com/itgeeks'
        ACCOUNT = 'whzhcahzxh@163.com'
        PASSWORD = 'huiyuanai'
        
        #for getting the authorize url
        client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
        url = client.get_authorize_url()
        print url
        conn = httplib.HTTPSConnection('api.weibo.com')
        postdata = urllib.urlencode({'client_id':APP_KEY,'response_type':'code','redirect_uri':CALLBACK_URL,'action':'submit','userId':ACCOUNT,
                                          'passwd':PASSWORD,'isLoginSina':0,'from':'','regCallback':'','state':'','ticket':'','withOfficalFlag':0})
        conn.request('POST','/oauth2/authorize',postdata,{'Referer':url,'Content-Type': 'application/x-www-form-urlencoded'})
        res = conn.getresponse()
        print 'headers===========',res.getheaders()
        print 'msg===========',res.msg
        print 'status===========',res.status
        print 'reason===========',res.reason
        print 'version===========',res.version
        location = res.getheader('location')
        print location
        code = location.split('=')[1]
        conn.close()
        
        r = client.request_access_token(code)
        access_token = r.access_token # The token return by sina
        expires_in = r.expires_in
        
        print "access_token=" ,access_token, "expires_in=" ,expires_in
        
        #save the access token
        client.set_access_token(access_token, expires_in)
        return client