import pyttsx3
import schedule
import time
from datetime import datetime
from RedditScraper import *


def find_between(s, start, end):
    return (s.split(start))[1].split(end)[0]


def runAlarm():
    newsReader = RedditScraper()
    engine = pyttsx3.init()
    currentTime = datetime.now().strftime("%m/%d/%Y")
    engine.say("It's time to wake up! Top Reddit news posts on the morning of " + currentTime)

    for subreddit in newsReader.subreddits:
        newsArticles = newsReader.compileNewsArticleHeadings(subreddit)
        engine.say("In subReddit " + subreddit)
        engine.runAndWait()
        for newsArticle in newsArticles:
            stringTag = find_between(str(newsArticle), ">", "<")
            engine.say(stringTag)
            engine.runAndWait()
    return


schedule.every().day.at("07:45").do(runAlarm())

while True:
    schedule.run_pending()
    time.sleep(60)

