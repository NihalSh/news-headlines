import feedparser

#model
class News:
    def __init__(self, headline, short_desc, url):
        assert type(headline) is unicode, "str expected"
        assert type(short_desc) is unicode, "str expected"
        assert type(url) is unicode, "str expected"
        self.headline = headline
        self.description = short_desc
        self.url = url

    def __str__(self):
        return "---\n" + self.headline + "\n\n" + self.description + "\n\n" + self.url + "\n---"

url = "http://feeds.bbci.co.uk/news/world/rss.xml"
d = feedparser.parse(url)

newsList = []
for entry in d.entries:
    headline = entry.title
    desc = entry.description
    url = entry.link
    newsList.append(News(headline, desc, url))

for news in newsList:
    print news
    
