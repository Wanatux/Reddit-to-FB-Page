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
reddit_list = ['nextfuckinglevel', 'instantkarma','ActualPublicFreakouts','Whatcouldgowrong','IdiotsInCars','Cringetopia','WinStupidPrizes', 'trashy','PublicFreakout', 'aww', 'Wellthatsucks', 'KidsAreFuckingStupid', 'therewasanattempt', 'instant_regret']
# reddit.read_only = True

#Praw Scrape
vids = []
Reddit_Scrapper = True

while Reddit_Scrapper:
    sub = r.subreddit(random.choice(reddit_list))
    posts = sub.hot(limit=10)    
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
        if vids[0][2] in df.values:
            list.remove(0)
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

#FB Credits and create Video Post
    
page_id_1 = 'Enter INT VALUE Here'
facebook_access_token_1 = 'Enter Info Here'
    
video_url = 'https://graph-video.facebook.com/v11.0/{}/videos'.format(page_id_1)
video_location = downloadlink
video_payload = {
'file_url': video_location,
'title': vids[0][0],
'description': vids[0][0],        
'access_token': facebook_access_token_1,

}

r = requests.post(video_url, data=video_payload)

print(r.text)