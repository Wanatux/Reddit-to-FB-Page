# Reddit to FB Page
 Python Script to scrape from Reddit Hot videos from specific subreddits and post them automatically to a FB Page.

Videos with audio from reddit to FB, I am not downloading the videos locally, I am getting the download link from reddit.tube and thats the value you can use to upload the content to a FB Page.

## Is it better than Zapier?

Is not going to post all the videos everytime you run it, some videos have good quality and FB will not let you upload that, probably I will see if I can implement that feature to auto resize videos but at the moment works the way its intended, Zapier also has a small percentage of failed posts from pictures and of course will not let you post videos with audio unless you have a premium membership.

## XLSX File? Why?
I am not sure why Im using a XLSX file to keep track of the historic posts in order to avoid duplicate posting, maybe I am used to excel and thats why I automatically started to keep track in it CSV file, anyways this is a script I was able to put together in a couple of hours, more updates and improvements will be posted regularly.

## Third Party API?
I am not using any third party API, I am using directly an app from reddit and FB.

## Config needed before start.
### Select your preffered Sub Reddits

Update the following code:

```
#SubReddit List
reddit_list = ['nextfuckinglevel', 'instantkarma','ActualPublicFreakouts','Whatcouldgowrong','IdiotsInCars','Cringetopia','WinStupidPrizes', 'trashy','PublicFreakout', 'aww', 'Wellthatsucks', 'KidsAreFuckingStupid', 'therewasanattempt', 'instant_regret']
```

### Reddit Creds
If you do now know how to get the requiered information please visit the following site:
https://www.reddit.com/prefs/apps

Update the following block.
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

Update the following block.
```
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
```
## How is this script able to post videos with audio to FB from Reddit?
Well I am using reddit.tube for that :smiley:


### Soon I will upload a guide explaining step by step how to set this up and use it as scheduled script.

https://wanatux.com
