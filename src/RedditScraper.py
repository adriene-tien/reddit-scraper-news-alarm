import requests
from bs4 import BeautifulSoup


class RedditScraper(object):

    def __init__(self):
        self.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                         'Chrome/75.0.3770.142 Safari/537.36 '
        self.redditUrl = 'https://www.reddit.com/'
        self.subreddits = ['r/news', 'r/worldnews', 'r/politics']
        self.headers = {
            'user-agent': self.userAgent
        }
        self.listToScan = []

    # function will search for reddit posts linked to songs, albums, etc.
    @staticmethod
    def findRelevantPosts(redditPageObject):
        relevantPosts = redditPageObject.findAll(
            lambda tag: tag.name == 'h3')
        print([x.text for x in relevantPosts])
        return relevantPosts

    def getPage(self, fullRedditUrl):
        rawPageData = requests.get(fullRedditUrl, headers=self.headers, timeout=20)

        if rawPageData.status_code != 200:
            print("Error loading page. HTTP status code: " + str(rawPageData.status_code))
            exit(rawPageData.status_code)

        soup = BeautifulSoup(rawPageData.content)

        if soup:
            return self.findRelevantPosts(soup)
        else:
            return False

    def compileNewsArticleHeadings(self, subreddit):
        # for subreddit in self.subreddits:
        fullRedditUrl = self.redditUrl + subreddit
        if self.getPage(fullRedditUrl) is False:
            exit("Could not successfully soupify page contents of " + fullRedditUrl)
        else:
            return self.getPage(fullRedditUrl)
