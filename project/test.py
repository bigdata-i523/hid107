# -*- coding: utf-8 -*-  
from weibo import APIClient
import webbrowser


APP_KEY = '2544974258' #geting App Key 
APP_SECRET = 'fa059ba3b637b24054804873337989c9' #geting AppSecret 
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html' #call back link, if you need this link, let me know

#using offical weibo SDK  
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)  
#open authorize page 
url = client.get_authorize_url()  
print url  
webbrowser.open_new(url)  
  
#get the authorize code
print 'please enter the code and press enter'  
code = raw_input()  
#code = your.web.framework.request.get('code')  
#client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)  
r = client.request_access_token(code)  
access_token = r.access_token # return the token  
expires_in = r.expires_in  
  
# set up the recied token 
client.set_access_token(access_token, expires_in)  
  
 
k = client.comments.show.get(id =4181049065748258 ,count = 150,page = 1)

for st in k.comments:
    text = st.user
    text2= st.text
    follower=text.followers_count #get the user followers num
    friends=text.friends_count #get the friends num
    feed=text.statuses_count # get the feed num
    f=open("follower.txt","a")
    f.write("'"+str(follower)+"' ")
    fr=open("friends.txt","a")
    fr.write("'"+str(friends)+"' ")
    fe=open("feed.txt","a")
    fe.write("'"+str(feed)+"' ")
    content=open("content.txt","a")
    content.write("'"+text2.encode("gb2312","ignore")+"' ")

