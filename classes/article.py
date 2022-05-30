import datetime

class Article:
    """
        This class represents an Article

        :author: Panda <panda@delmasweb.net>
        :date: 30 May 2022
        :version: 1.0
    """

    def __init__(self, title : str = "NO_TITLE", description : str = "", authors : list = list(), link : str = "", date : datetime.date = datetime.date.today()) -> None:
        """
            Constructor

            :param title: The title of article
            :type title: str
            :param authors: The authors of the article
            :type authors: list
            :param link: The link of the full article
            :type link: str
            :param description: The short description
            :type description: str
            :param date: The date of the article
            :type date: DateTime 
        """
        self.title = title
        self.description = description
        self.authors = authors
        self.link = link
        self.date = date

    def __str__(self) -> str:
        return f"Title : [{self.title}], Description : [{self.description}], Authors : [{self.authors}], Link : [{self.link}], Date : [{self.date}]"