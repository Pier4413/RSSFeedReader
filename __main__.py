
from modules.logger.logger import Logger

from classes.feed import Feed
from classes.article import Article

# Load the logger
Logger.get_instance().load_logger("RSS Feed", console=True, level=10)

feed = Feed("https://www.courrierinternational.com/feed/category/6260/rss.xml")
feed.readFeed(3)

try:
    Logger.get_instance().debug(feed.getFeedByIndex(0))
except Exception as e:
    Logger.get_instance().critical(f"Could not parse the test {e}")