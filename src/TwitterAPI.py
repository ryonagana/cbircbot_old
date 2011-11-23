'''
Created on 23/11/2011

@author: Nicholas
'''
import twitter, os,sys

class TwitterAuth(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        
        
class TwitterAPI(object):
    def __init__(self, authclass):
        self.api = twitter.Api(authclass.consumer_key, authclass.consumer_secret, authclass.access_token, authclass.access_token_secret)
        
        if( self.api.VerifyCredentials() != None ):
            self.friendlist = self.api.GetFriends()
        else:
            sys.stderr << "Twitter API Failed Credentials"
            
    def getFriendList(self):
        
        friends = []
        
        for friend in self.friendlist:
            friends.append(friend.name)
        
        return friends
    
    def doTweet(self, message, args = None):
        
        
        if( len(message) <= 140):
            self.api.PostUpdates(message,args)
            
        