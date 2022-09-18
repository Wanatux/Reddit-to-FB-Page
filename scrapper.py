import praw
import random
import pandas as pd
import config
import requests
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
options.add_argument('window-size=1200x1040')
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
options.add_argument('user-agent={0}'.format(user_agent))

r = praw.Reddit(
    client_id= ,
    client_secret= ,
    user_agent= ,
    username= ,
    password= ,
    )      
class RedditScrap:
    def __init__(self):
        self.picscrap = self.picscrap()
        self.vidscrap = self.vidscrap()
        pass


    def fb_descript( x, y):
        tags = []
        s = ' '
        for x in x.split():
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
        {d}    
        {b}'''.format(a=x, b=s, c='.' * 5, d=y)

    def picscrap():
        # SubReddit List
        reddit_list = config.subreddit_list
        # Praw Scrape
        posts = []
        reddit_scrapper = True

        while reddit_scrapper:
            subreddit = r.subreddit(random.choice(reddit_list))
            for submission in subreddit.hot(limit=10):
                try:
                    if 'jpg' not in submission.url:
                        continue
                    if submission.stickied:
                        continue
                    pic_tittle = submission.title
                    url = submission.url
                    auth = submission.author
                    un_id = submission.id
                    posts.append((pic_tittle, url, un_id, auth))
                except:
                    pass
                # Check if post was already posted

                df = pd.read_csv('/home/devel/code/social/log.csv')

                checker = True
                while checker:
                    if len(posts) == 0:
                        checker = False
                    if posts[0][2] in df.values:
                        posts.pop(0)
                        if len(posts) == 0:
                            checker = False
                    else:
                        checker = False
                if len(posts) > 1:
                    reddit_scrapper = False

                # If data doesnt exist then append row
        df2 = pd.DataFrame({'un_id': [posts[0][2]],
                            'pic_tittle': [posts[0][0]]})

        df3 = pd.concat([df, df2])
        df3.to_csv('/home/devel/code/social/log.csv')




        # FB Credits and Photo Post

        def postInstagramQuote():
            # Post the Image
            image_location_1 = posts[0][1]
            post_url = 'https://graph.facebook.com/v10.0/{}/media'.format(config.inst_id)
            payload = {
                'image_url': image_location_1,
                'caption': RedditScrap.fb_descript(posts[0][0], posts[0][3]),
                'access_token': config.inst_acc_token,
            }
            r = requests.post(post_url, data=payload)
            #  print(r.text)

            result = json.loads(r.text)
            if 'id' in result:
                creation_id = result['id']
                second_url = 'https://graph.facebook.com/v10.0/{}/media_publish'.format(config.inst_id)
                second_payload = {
                    'creation_id': creation_id,
                    'access_token': config.inst_acc_token,
                }
                r = requests.post(second_url, data=second_payload)
            #        print('--------Just posted to instagram--------')
            #        print(r.text)
            else:
                pass


        def post_FBpage():
            image_url = 'https://graph.facebook.com/{}/photos'.format(config.fb_page_id)
            image_location = posts[0][1]
            msg = RedditScrap.fb_descript(posts[0][0], posts[0][3])
            img_payload = {
                'message': msg,
                'url': image_location,
                'access_token': config.fb_acc_token
            }
            # Send the POST request
            r = requests.post(image_url, data=img_payload)


        #    print('--------Just posted to Facebook--------')
        #    print(r.text)
        post_FBpage()
        postInstagramQuote()


    def vidscrap():
        # Reddit Creds

        # SubReddit List
        reddit_list = config.subreddit_list
        # reddit.read_only = True

        # Praw Scrape
        posts = []
        reddit_scrapper = True

        while reddit_scrapper:
            sub = r.subreddit(random.choice(reddit_list))
            posts1 = sub.hot(limit=20)
            for p in posts1:
                try:
                    url = p.secure_media['reddit_video']['fallback_url']
                    name = "https://www.reddit.com/" + p.permalink
                    post_tittle = p.title
                    un_id = p.id
                    auth = p.author
                    posts.append((post_tittle, name, un_id, auth))
                except:
                    pass

            # Check if post was already posted
            # If it doesnt exist in Excel then continue
            df = pd.read_csv('/home/devel/code/social/log2.csv')

            checker = True
            while checker:
                if len(posts) == 0:
                    checker = False
                    break
                if posts[0][2] in df.values:
                    posts.pop(0)
                    if len(posts) == 0:
                        checker = False
                else:
                    checker = False
            if len(posts) > 1:
                reddit_scrapper = False

            # If data doesnt exist then append row
        df2 = pd.DataFrame({'ID': [posts[0][2]],
                            'Title': [posts[0][0]]})

        df3 = pd.concat([df, df2])
        df3.to_csv('/home/devel/code/social/log2.csv')

        # Get download link from reddit.tube
        link = posts[0][1]
        link = link.replace(".com", ".tube")

        driver_path = 'chromedriver'
        driver = webdriver.Chrome(options=options, executable_path=driver_path)
        driver.get(link)

        links = driver.find_element(by=By.XPATH, value="//*[@id='response-link']")
        time.sleep(3)

        downloadlink = links.get_attribute("href")

        driver.quit()


        # FB Credits and Photo Post

        def postInstagramVideo():
            # Post the Image
            video_location_1 = downloadlink
            post_url = 'https://graph.facebook.com/v10.0/{}/media'.format(config.inst_id)
            payload = {
                'media_type': 'VIDEO',
                'video_url': video_location_1,
                'caption': RedditScrap.fb_descript(posts[0][0], posts[0][3]),
                'access_token': config.inst_acc_token,
            }
            r = requests.post(post_url, data=payload)
            # print(r.text)

            result = json.loads(r.text)
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


        # print('HOUSTON we have a problem')
        postInstagramVideo()


        def postFacebookVideo():
            video_url = 'https://graph-video.facebook.com/v11.0/{}/videos'.format(config.fb_page_id)
            video_location = downloadlink
            video_payload = {
                # 'upload_phase': 'start',
                'file_url': video_location,
                'title': posts[0][0],
                'description': RedditScrap.fb_descript(posts[0][0], posts[0][3]),
                'access_token': config.fb_acc_token,

            }
            r = requests.post(video_url, data=video_payload)
            print('--------Just posted to Facebook--------')
            print(r.text)


        postFacebookVideo()
RedditScrap.picscrap()
RedditScrap.vidscrap()
