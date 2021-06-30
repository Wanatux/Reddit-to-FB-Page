#Clean Code Video Download Link for any social media
import praw
import time
import random
import requests
import pandas as pd
from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True

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
# reddit.read_only = True

#Praw Scrape
vids = []
Reddit_Scrapper = True

while Reddit_Scrapper:
    sub = r.subreddit(random.choice(reddit_list))
    posts = sub.hot(limit=20)    
    for p in posts:
        try:
            url = p.secure_media['reddit_video']['fallback_url']
            name = "https://www.reddit.com/" + p.permalink
            post_tittle = p.title
            un_id = p.id        
            vids.append((post_tittle, name, un_id))
        except:
            pass

    #Check if post was already posted
    #If it doesnt exist in Excel then continue
    df = pd.read_excel(r'subrreddit_history.xlsx')

    checker = True
    while checker:
        if len(vids) == 0:
            checker = False
            break
        if vids[0][2] in df.values:
            vids.pop(0)
            if len(vids) == 0:
                checker = False
        else:
            checker = False 
    if len(vids) > 1:
        Reddit_Scrapper = False            

# If data doesnt exist then append row
df = pd.DataFrame({'ID': [vids[0][2]],
                   'Title': [vids[0][0]]})
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

#Get download link from reddit.tube
link = vids[0][1]
link = link.replace(".com" , ".tube")

DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get(link)

links = driver.find_elements_by_xpath("//*[@id='response-link']") 
time.sleep(3)

for link in links:
    downloadlink = link.get_attribute("href")
driver.quit()

writer.close()

#Creation of the description and Tags
def fb_descript():
    tags = []
    s = ' '
    for x in vids[0][0].split():
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
    {b}'''.format(a=vids[0][0], b=s, c='.' *5)
#FB Credits and Photo Post

def postInstagramVideo():
#Post the Image
    video_location_1 = downloadlink
    post_url = 'https://graph.facebook.com/v10.0/{}/media'.format(config.inst_id)
    payload = {
        'media_type': 'VIDEO',
        'video_url': video_location_1,
        'caption': fb_descript(),
        'access_token': config.inst_acc_token,
        }
    r = requests.post(post_url, data=payload)
    print(r.text)
    
    result = json.loads(r.text)
    #After the response you need to wait some secs for the second request.
    time.sleep(15)
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
postInstagramVideo()

def postFacebookVideo():
    video_url = 'https://graph-video.facebook.com/v11.0/{}/videos'.format(config.fb_page_id)
    video_location = downloadlink
    video_payload = {
    # 'upload_phase': 'start',
    'file_url': video_location,
    'title': vids[0][0],
    'description': vids[0][0],        
    'access_token': config.fb_acc_token,

    }
    r = requests.post(video_url, data=video_payload)
    print('--------Just posted to Facebook--------')
    print(r.text)
postFacebookVideo()    