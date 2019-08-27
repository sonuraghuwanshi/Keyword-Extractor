from __future__ import absolute_import
from __future__ import print_function
from tkinter import *
import six
import rake
import operator
import io
import urllib.request
import urllib.parse
import re
import webbrowser


def search():
    text=tbox1.get()
    print(text)
    stoppath = "data/stoplists/SmartStoplist.txt"
    rake_object = rake.Rake(stoppath, 5, 3, 4)
    keywords = rake_object.run(text)
    print("Keywords:", keywords)
    l = (len(keywords))
    print(l)
    for i in keywords:
        x = i
        print(x[0])
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")
        query = x[0]
        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            print(j)
            url = j
            values = {'s': 'basics',
                      'submit': 'search'}
            data = urllib.parse.urlencode(values)
            data = data.encode('utf-8')
            req = urllib.request.Request(url, data)
            resp = urllib.request.urlopen(req)
            respData = resp.read()
            paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
            for eachP in paragraphs:
                print(eachP)





root = Tk()
root.title("Test")
frame=Frame(root, width=500, height=500)
frame.pack()
text1 = Label(text="Enter the text to find the Keyword:-")
text1.place(x=10, y=10)
tbox1 = Entry(root)
tbox1.place(x=10, y=40, height=100, width=500)
button = Button(root, text='Search', width=25, command=search)
button.place(x=150,y=150)
#button.pack()
root.mainloop()