#Clean Code for Picture uploader for social media platform
import praw
import random
import pandas as pd
import config
from openpyxl import load_workbook
import requests
import json

#Reddit Creds
r = praw.Reddit(
    client_id= "Enter Info Here",
    client_secret= "Enter Info Here",
    user_agent= "Enter Info Here",
    username= "Enter Info Here",
    password= "Enter Info Here",
)

#SubReddit List
reddit_list = config.subreddit_list
#Praw Scrape
pics = []
Reddit_Scrapper = True

while Reddit_Scrapper:
    subreddit = r.subreddit(random.choice(reddit_list))
    for submission in subreddit.hot(limit=10):
        try:
            if 'jpg' not in submission.url:
                continue
            if submission.stickied:
                continue
            pic_tittle = submission.title
            url = submission.url
            un_id = submission.id
            pics.append((pic_tittle, url, un_id))
        except:
            pass
        #Check if post was already posted
        #If it doesnt exist in Excel then continue
        df = pd.read_excel(r'subrreddit_history.xlsx')

        checker = True
        while checker:
            if len(pics) == 0:
                checker = False
            if pics[0][2] in df.values:
                pics.pop(0)
                if len(pics) == 0:
                    checker = False                
            else:
                checker = False 
        if len(pics) > 1:
            Reddit_Scrapper = False   
        
# If data doesnt exist then append row
df = pd.DataFrame({'un_id': [pics[0][2]],
                   'pic_tittle': [pics[0][0]]})
writer = pd.ExcelWriter('subrreddit_history.xlsx', engine='openpyxl')
# try to open an existing workbook
writer.book = load_workbook('subrreddit_history.xlsx')
# copy existing sheets
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# read existing file
reader = pd.read_excel(r'subrreddit_history.xlsx')
# write out the new sheet
df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

writer.close()

#this will get the Tittle of the post split it and add #s ad the beggining of each word for Tags.
def fb_descript():
    tags = []
    s = ' '
    for x in pics[0][0].split():
        tags.append('#' + x)

    s = s.join(tags)

    return ''' {a} 
    {c}
    {c}
    {c}
    {c}
    {c}
    {c}
    {c}
    {c}
    {c}
    {c}    
    {b}'''.format(a=pics[0][0], b=s, c='.' *5)
#FB Credits and Photo Post

#INstagram Post Def
def postInstagramPic():
#Post the Image
    image_location_1 = pics[0][1]
    post_url = 'https://graph.facebook.com/v10.0/{}/media'.format(config.inst_id)
    payload = {
        'image_url': image_location_1,
        'caption': fb_descript(),
        'access_token': config.inst_acc_token,
        }
    r = requests.post(post_url, data=payload)
    print(r.text)
#Instagram for some reason will need to convert the responde ID to a publish request.    
    result = json.loads(r.text)
    if 'id' in result:
        creation_id = result['id']
        second_url = 'https://graph.facebook.com/v10.0/{}/media_publish'.format(config.inst_id)
        second_payload = {
        'creation_id': creation_id,
        'access_token': config.inst_acc_token,
        }
        r = requests.post(second_url, data=second_payload)
        print('--------Just posted to instagram--------')
        print(r.text)
    else:
        pass
postInstagramPic()

#Facebook Picture Def
def post_FBpage():   
    image_url = 'https://graph.facebook.com/{}/photos'.format(config.fb_page_id)
    image_location = pics[0][1]
    msg = fb_descript()
    img_payload = {
    'message': msg,    
    'url': image_location,
    'access_token': config.fb_acc_token
    }
    #Send the POST request
    r = requests.post(image_url, data=img_payload)
    print('--------Just posted to Facebook--------')
    print(r.text)
post_FBpage() 