# Reddit to FB Page and IG
 Python Script to scrape from Reddit Hot videos and Hot Pics from specific subreddits and post them automatically to a FB Page and IG.

Videos with audio from reddit to FB and IG, I am not downloading the videos locally, I am getting the download link from reddit.tube and thats the value you can use to upload the content to a FB Page.

IG only accepts specific format of videos and since the script will get a list and randomly choose a hot video for posting it might encounter some errors of posting, so far this script is posting 2/5 videos from my random list of subreddits, FB will post 4/5.

## Is it better than Zapier?

Is not going to post all the videos everytime you run it, some videos have good quality and FB will not let you upload that, probably I will see if I can implement that feature to auto resize videos but at the moment works the way its intended, Zapier also has a small percentage of failed posts from pictures and of course will not let you post videos with audio unless you have a premium membership.

## XLSX File? Why?
I am not sure why Im using a XLSX file to keep track of the historic posts in order to avoid duplicate posting, maybe I am used to excel and thats why I automatically started to keep track in it CSV file, anyways this is a script I was able to put together in a couple of hours, more updates and improvements will be posted regularly.

## Third Party API?
I am not using any third party API, I am using directly an app from reddit, FB and IG.

## Config needed before start.
### Select your preffered Sub Reddits

Update the following code from the config file:

```
#SubReddit List
reddit_list = ['nextfuckinglevel', 'instantkarma','ActualPublicFreakouts','Whatcouldgowrong','IdiotsInCars','Cringetopia','WinStupidPrizes', 'trashy','PublicFreakout', 'aww', 'Wellthatsucks', 'KidsAreFuckingStupid', 'therewasanattempt', 'instant_regret']
```

### Reddit Creds
If you do now know how to get the requiered information please visit the following site:
https://www.reddit.com/prefs/apps

Update the following block.
You can also edit or add your info in PRAW.ini if you dont want to insert your creds in the code but for this script I m using the reddit credentials on top of the code.
```
#Reddit Creds
r = praw.Reddit(
    client_id= "Enter Info Here",
    client_secret= "Enter Info Here",
    user_agent= "Enter Info Here",
    username= "Enter Info Here",
    password= "Enter Info Here",
)

```

### FB Creds
If you do now know how to get the requiered information please visit the following site:
https://developers.facebook.com/apps

Update the following in the config file.
```
#Facebook
fb_acc_token = ' ' #Enter Access Token Here
fb_page_id = ' ' #Get Page ID Here

}
```

### IG Creds
If you do now know how to get the requiered information please visit the following site:
https://developers.facebook.com/apps

If you are creating the IG app first you can use the same access token for FB and IG.

Update the following in the config file.
```
#Instagram
inst_acc_token = ' ' #INstagram Access Token, it can be used for FB Page as well if you have the right permissions
inst_id = ' ' #Insta Page ID

```
## How is this script able to post videos with audio to FB from Reddit?
Well I am using reddit.tube for that :smiley:


### Soon I will upload a guide explaining step by step how to set this up and use it as scheduled script.

https://wanatux.com
