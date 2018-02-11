import pyttsx3
import time
import nltk

import requests
from io import BytesIO

import PIL.Image
import PIL.ImageTk


import matplotlib.pyplot as plt
from flickrapi import FlickrAPI
import numpy as np
import urllib.request
import cv2

from tkinter import *
import tkinter

def text2Speech(sentence):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    voices = engine.getProperty('voices')

    # +f2 raises frequency. More pleasant voice.
    engine.setProperty('voice', 'english+f3')
    engine.setProperty('rate', rate - 50)

    engine.say(sentence)

    engine.runAndWait()


def get_best_word(sentence):
    sentence = nltk.tokenize.word_tokenize(sentence)
    return sentence

# Takes in the sentence. Calculates the best noun to display as an image and goes and gets it using bing image search
# and then displays it.
def display_picture(sentence, app):
    search_term = get_best_word(sentence)

    app.switch_picture(search_term)

    #display(image) <--- got to figure out how to display? on python gui or java?


def getImage(search_term):
    subscription_key = 'ecda2ab9abe346a0a2c8610fdc99ad54'
    assert subscription_key

    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "license": "public", "imageType": "photo"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:16]]

    image_data = requests.get(thumbnail_urls[0])
    image_data.raise_for_status()
    image = PIL.Image.open(BytesIO(image_data.content))

    return image

'''
img = getImage()

img.show()
'''

class FullScreenApp(object):


    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)

        master.title("Imagination Unleashed")
        self.label = Label(master, text="Welcome to Imagination Unleashed! Please select the type of story you'd like!")
        self.label.pack()

        types = ["alice and wonderland", "harry potter", "pirates"]
        for type in types:
            self.type = Button(master, text=type, command=self.start)
            self.type.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.start_button = Button(master, text="Go!", command=self.start)
        self.start_button.pack()

        image = getImage("santa")

        img = PIL.ImageTk.PhotoImage(image)
        self.panel = tkinter.Label(root, image=img)
        self.panel.place(x=700, y=300)
        self.panel.configure(image = img)
        self.panel.image = img

    def switch_picture(self, search_term):
        print("switching")
        image2 = getImage(search_term)
        image2 = PIL.ImageTk.PhotoImage(image2)
        self.panel.configure(image=image2)
        self.panel.image = image2
        self.panel.place(x=700, y=300)

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

    def start(self):
        # somehow need to get the type from this.
        print(self)


root=Tk()
app=FullScreenApp(root)
root.mainloop()
#app.switch_picture(search_term)

file = open('generated_story.txt', 'r').readlines()

for sentence in file:
    display_picture(sentence, app)
    text2Speech(sentence[1:-3]) #Reads the sentence outloud
    time.sleep(1)

'''
def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    #image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = Image.fromarray(image, 'RGB')

    return image




FLICKR_PUBLIC = '6fdf088b862a49a3ae1e678296c00936'
FLICKR_SECRET = '605ede6b9004a09e'

flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'

cats = flickr.photos.search(tags='grass', per_page=5, extras=extras)

photos = cats['photos']
from pprint import pprint
pprint(photos)

photoUrl = photos['photo'][0]['url_m']

response = requests.get(photoUrl)
image = Image.open(BytesIO(response.content))



#image = url_to_image(photoUrl)

#cv2.imshow("Image", image)
#cv2.waitKey(0)

#image.show()

'''


''' Text to speech stuff
from urllib import request

url = "https://www.gutenberg.org/files/11/11.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')


engine = pyttsx3.init()

rate = engine.getProperty('rate')
voices = engine.getProperty('voices')

# +f2 raises frequency. More pleasant voice.
engine.setProperty('voice', 'english+f3')
engine.setProperty('rate', rate-50)

engine.say(raw[:250])

engine.runAndWait()
'''
