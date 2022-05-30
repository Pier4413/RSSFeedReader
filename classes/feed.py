import datetime
import feedparser

from classes.article import Article

from modules.logger.logger import Logger

class Feed:
    """
        This class represents a feed (URL, ...)

        :author: Panda <panda@delmasweb.net>
        :date: 30 May 2022
        :version: 1.0
    """

    def __init__(self, url : str) -> None:
        """
            Constructor

            :param url: The url of the feed
            :type url: str
        """
        self.url = url
        self.feeds = list()

    def __str__(self) -> str:
        return f"The URL of this feed is : {self.url}"

    def __eq__(self, __o: object) -> bool:
        """
            This function returns if two feeds are the same based on the URL

            :param __o: The object to compare against
        """
        if(hasattr(__o, "url")):
            return self.url.__eq__(__o.url)
        else:
            return False

    def readFeed(self, size : int) -> None:
        """
            Get the list of the latest news by the size size
        """
        body = feedparser.parse(self.url)
        
        self.feeds.clear()
        
        if(len(body.entries) < size):
            Logger.get_instance().warning(f"The asked size {size} is higher than the provided by the feed {len(body.entries)}, will only provide {len(body.entries)}")
            size = len(body.entries)

        for i in range(0, size):
            article = Article(title=body.entries[i].title,
                link=body.entries[i].link,
                date=datetime.date(body.entries[i].published_parsed[0], body.entries[i].published_parsed[1], body.entries[i].published_parsed[2]))
            self.feeds.append(article)

    def getFeedByIndex(self, index : int) -> Article:
        return self.feeds[index]