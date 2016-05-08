from bs4 import BeautifulSoup
from Tkinter import *
import ttk
import urllib3
import webbrowser

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
        return unicode("---\n" + self.headline + "\n\n" + self.description + "\n\n" + self.url + "\n---").encode('utf-8')

def test():
    print "hello"

class Interface:
    def __init__(self, master):
        self.currentindex = [0, 0, 0, 0, 0]

        master.title('News Headlines')
        master.resizable(False, False)
        master.configure(background = '#4DD0E1')
        #master.configure(background = '#607D8B')

        self.style = ttk.Style()
        """
        self.style.configure('TFrame', background = '#78909C')
        self.style.configure('Header.TFrame', background = '#607D8B')
        self.style.configure('Button.TFrame', background = '#607D8B')
        self.style.configure('TButton', background = '#90A4AE')
        self.style.configure('TLabel', foreground = '#000000', background = '#78909C', font = ('Arial', 11))
        self.style.configure('Headline.TLabel', foreground = '#000000', background = '#78909C', font = ('Arial', 11, 'bold'))
        self.style.configure('Header.TLabel', foreground = '#000000', background = '#78909C', font = ('Arial', 18, 'bold'))
        """
        self.style.configure('TFrame', background = '#E0F7FA')
        self.style.configure('Header.TFrame', background = '#000000')
        self.style.configure('Logo.Header.TFrame')
        self.style.configure('Button.TFrame', background = '#4DD0E1')
        self.style.configure('TButton', foreground = '#FFFFFF', background = '#000000', font = ('Arial', 11, 'bold'))
        self.style.map('TButton', foreground = [('hover', '#FFFFFF'), ('pressed', '#FFFFFF')], background = [('hover', '#000000'), ('pressed', '#000000')])
        self.style.configure('TLabel', foreground = '#000000', background = '#E0F7FA', font = ('Arial', 11))
        self.style.configure('Title.TLabel', foreground = '#FFFFFF', background = '#000000', font = ('Arial', 22, 'bold'))
        self.style.configure('Subtitle.TLabel', foreground = '#FFFFFF', background = '#000000', font = ('Arial', 11, 'bold'))
        
        self.style.configure('Headline.TLabel', foreground = '#000000', background = '#E0F7FA', justify = CENTER, font = ('Arial', 13, 'bold'), wraplength = 300)
        
        self.frame_header = ttk.Frame(master, padding='0.1i', style = 'Header.TFrame')
        self.frame_header.pack(fill="both", expand=True)

        #self.logo = PhotoImage(file = 'logo.gif')
        #ttk.Label(self.frame_header, style = 'Logo.Header.TFrame', image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'News Headlines', style = 'Title.TLabel').pack()#grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300, style = "Subtitle.TLabel",
                  text = "A quick way a catch up on the latest news!").pack()#grid(row = 1, column = 1)

        #self.canvas = Canvas(master, bg = '#e1d8b9')
        #self.canvas.pack(side = RIGHT, fill = BOTH, expand = True)

        #News Item 1 -> Begin
        self.frame_contentHolder = ttk.Frame(master)
        self.frame_content1 = ttk.Frame(self.frame_contentHolder, padding='0.1i', relief=RAISED)

        self.label_title1 = ttk.Label(self.frame_content1, text = 'Headline1', style = 'Headline.TLabel')
        bindtags = list(self.label_title1.bindtags())
        bindtags.insert(1, self.frame_content1)
        self.label_title1.bindtags(tuple(bindtags))

        self.label_shortDescription1 = ttk.Label(self.frame_content1, wraplength = 300, text = "Content goes here1")
        bindtags = list(self.label_shortDescription1.bindtags())
        bindtags.insert(1, self.frame_content1)
        self.label_shortDescription1.bindtags(tuple(bindtags))

        self.label_title1.pack()
        self.label_shortDescription1.pack()
        self.frame_content1.pack(fill="both", expand=True)

        self.frame_content1.bind('<ButtonPress>', lambda e: self.callback_openBrowser(e, 0))
        self.frame_content1.bind('<ButtonRelease>', lambda e: self.callback_revertStyle(e, 0))

        #News Item 2 -> Begin
        self.frame_content2 = ttk.Frame(self.frame_contentHolder, padding='0.1i', relief=RAISED)

        self.label_title2 = ttk.Label(self.frame_content2, text = 'Headline2', style = 'Headline.TLabel')
        bindtags = list(self.label_title2.bindtags())
        bindtags.insert(1, self.frame_content2)
        self.label_title2.bindtags(tuple(bindtags))

        self.label_shortDescription2 = ttk.Label(self.frame_content2, wraplength = 300, text = "Content goes here2")
        bindtags = list(self.label_shortDescription2.bindtags())
        bindtags.insert(1, self.frame_content2)
        self.label_shortDescription2.bindtags(tuple(bindtags))

        self.label_title2.pack()
        self.label_shortDescription2.pack()
        self.frame_content2.pack(fill="both", expand=True)

        self.frame_content2.bind('<ButtonPress>', lambda e: self.callback_openBrowser(e, 1))
        self.frame_content2.bind('<ButtonRelease>', lambda e: self.callback_revertStyle(e, 1))

        #News Item 3 -> Begin
        self.frame_content3 = ttk.Frame(self.frame_contentHolder, padding='0.1i', relief=RAISED)

        self.label_title3 = ttk.Label(self.frame_content3, text = 'Headline3', style = 'Headline.TLabel')
        bindtags = list(self.label_title3.bindtags())
        bindtags.insert(1, self.frame_content3)
        self.label_title3.bindtags(tuple(bindtags))

        self.label_shortDescription3 = ttk.Label(self.frame_content3, wraplength = 300, text = "Content goes here3")
        bindtags = list(self.label_shortDescription3.bindtags())
        bindtags.insert(1, self.frame_content3)
        self.label_shortDescription3.bindtags(tuple(bindtags))

        self.label_title3.pack()
        self.label_shortDescription3.pack()
        self.frame_content3.pack(fill="both", expand=True)

        self.frame_content3.bind('<ButtonPress>', lambda e: self.callback_openBrowser(e, 2))
        self.frame_content3.bind('<ButtonRelease>', lambda e: self.callback_revertStyle(e, 2))

        #News Item 4 -> Begin
        self.frame_content4 = ttk.Frame(self.frame_contentHolder, padding='0.1i', relief=RAISED)

        self.label_title4 = ttk.Label(self.frame_content4, text = 'Headline4', style = 'Headline.TLabel')
        bindtags = list(self.label_title4.bindtags())
        bindtags.insert(1, self.frame_content4)
        self.label_title4.bindtags(tuple(bindtags))

        self.label_shortDescription4 = ttk.Label(self.frame_content4, wraplength = 300, text = "Content goes here4")
        bindtags = list(self.label_shortDescription4.bindtags())
        bindtags.insert(1, self.frame_content4)
        self.label_shortDescription4.bindtags(tuple(bindtags))

        self.label_title4.pack()
        self.label_shortDescription4.pack()
        self.frame_content4.pack(fill="both", expand=True)

        self.frame_content4.bind('<ButtonPress>', lambda e: self.callback_openBrowser(e, 3))
        self.frame_content4.bind('<ButtonRelease>', lambda e: self.callback_revertStyle(e, 3))

        #News Item 5 -> Begin
        self.frame_content5 = ttk.Frame(self.frame_contentHolder, padding='0.1i', relief=RAISED)

        self.label_title5 = ttk.Label(self.frame_content5, text = 'Headline5', style = 'Headline.TLabel')
        bindtags = list(self.label_title5.bindtags())
        bindtags.insert(1, self.frame_content5)
        self.label_title5.bindtags(tuple(bindtags))

        self.label_shortDescription5 = ttk.Label(self.frame_content5, wraplength = 300, text = "Content goes here5")
        bindtags = list(self.label_shortDescription5.bindtags())
        bindtags.insert(1, self.frame_content5)
        self.label_shortDescription5.bindtags(tuple(bindtags))

        self.label_title5.pack()
        self.label_shortDescription5.pack()
        self.frame_content5.pack(fill="both", expand=True)

        self.frame_contentHolder.pack(fill="both", expand=True)

        self.frame_content5.bind('<ButtonPress>', lambda e: self.callback_openBrowser(e, 4))
        self.frame_content5.bind('<ButtonRelease>', lambda e: self.callback_revertStyle(e, 4))

        self.frames = (self.frame_content1, self.frame_content2, self.frame_content3, self.frame_content4, self.frame_content5)
        self.titles = (self.label_title1, self.label_title2, self.label_title3, self.label_title4, self.label_title5)
        self.description = (self.label_shortDescription1, self.label_shortDescription2, self.label_shortDescription3, self.label_shortDescription4, self.label_shortDescription5)

        self.frame_navigation = ttk.Frame(master, padding='0.1i', style = 'Button.TFrame')
        self.next = ttk.Button(self.frame_navigation, text = 'Next', command = lambda : self.callback_newsItem(index = self.currentindex[0] + 5, next = True))
        self.next.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = 'e')

        self.previous = ttk.Button(self.frame_navigation, text = 'Previous', command = lambda : self.callback_newsItem(index = self.currentindex[0] - 5, next = False))
        self.previous.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'w')
        self.frame_navigation.pack()

        self._getNews()

    def callback_openBrowser(self, event, index):
        self.frames[index].configure(relief=SUNKEN)

    def callback_revertStyle(self, event, index):
        webbrowser.open_new(self.newsList[self.currentindex[index]].url)
        self.frames[index].configure(relief=RAISED)

    def callback_newsItem(self, event = None, index = 0, next = True):
        #if next == False:
        #    index - 6

        for i in xrange(index, index + 5):
            frameNumber = abs(i - index)
            #print frameNumber
            #self.currentindex[i - index - 1] = i
            if i < len(self.newsList) and i >= 0:
                self.titles[frameNumber].configure(text=self.newsList[i].headline);#change
                self.description[frameNumber].configure(text=self.newsList[i].description);#change
                self.currentindex[frameNumber] = i
        index = index + 5
        #print index
        if index < 10:
            #disable prev
            self.previous.state(['disabled'])
        else:
            self.previous.state(['!disabled'])
            #enable prev

        if index > len(self.newsList):
            #disable next
            self.next.state(['disabled'])
        else:
            self.next.state(['!disabled'])

    def _getNews(self):
        url = "http://feeds.bbci.co.uk/news/world/rss.xml"
        d = FeedParser(url)

        self.newsList = []
        for entry in d.entries:
            headline = entry['title']
            desc = entry['description']
            url = entry['link']
            self.newsList.append(News(headline, desc, url))

        self.callback_newsItem()
"""
        self.label_title1.configure(text=self.newsList[0].headline);#change
        self.label_shortDescription1.configure(text=self.newsList[0].description);#change
        self.label_title2.configure(text=self.newsList[1].headline);#change
        self.label_shortDescription2.configure(text=self.newsList[1].description);#change
        self.label_title3.configure(text=self.newsList[2].headline);#change
        self.label_shortDescription3.configure(text=self.newsList[2].descrition);#change
"""

class FeedParser:
    def __init__(self, url):
        http = urllib3.PoolManager()
        r = http.request('GET', url)
        self.entries = []
        if r.status == 200:
            soup = BeautifulSoup(r.data, 'html.parser')
            items = soup.find_all('item')
            for item in items:
                entry = {}
                entry['title'] = item.title.get_text()
                entry['description'] = item.description.get_text()
                entry['link'] = item.link.get_text()
                self.entries.append(entry.copy())

def main():
    root = Tk()
    interface = Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
