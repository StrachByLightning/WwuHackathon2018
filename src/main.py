import pyttsx3
import time
import nltk

import requests
from io import BytesIO

import PIL.Image
import PIL.ImageTk

import operator

from bingtts import Translator
import pygame

import os

from tkinter import *
import tkinter

from bin import getStory, docFormatter, modelGenerator, driver, speechOutput


getStory.getStory()


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
    frequency = {}
    for word in sentence:
        if word in frequency and word.isalpha():
            frequency[word] += 1
        else:
            frequency[word] = 1

    sorted_words = sorted(frequency.items(), reverse=True, key=operator.itemgetter(1))

    return sorted_words[0][0]

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

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)

        master.title("Pure Imagination Unleashed")
        self.label = Label(master, text="Welcome to Pure Imagination Unleashed! Please select the type of story you'd like!")
        self.label.pack()

        # Generate drop down to select type
        all_stories = self.all_stories()
        variable = StringVar(master)
        variable.set(all_stories[0])

        menu = OptionMenu(master, variable, all_stories[0], all_stories[1], all_stories[2], command=self.start_storytime)
        menu.pack()

        '''
        self.start_button = Button(master, text="Go!", command=self.start_storytime)
        self.start_button.pack()
        '''

        image = getImage("Book")

        img = PIL.ImageTk.PhotoImage(image)
        self.panel = tkinter.Label(root, image=img)
        self.panel.place(x=700, y=300)
        self.panel.configure(image = img)
        self.panel.image = img

    def all_stories(self):
        #os.chdir('resources')
        print(os.getcwd())
        file = open('listOfFiles.txt', 'r')
        all_stories = []

        for story in file:
            if story == '\n':
                continue
            all_stories.append(story)

        return all_stories


    def switch_picture(self, search_term):
        print("switching")
        print(search_term)
        image2 = getImage(search_term)
        image2 = PIL.ImageTk.PhotoImage(image2)
        self.panel.configure(image=image2)
        self.panel.image = image2
        self.panel.place(x=700, y=100)

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

    def start_storytime(self, textfile):
        # Call the function to generate a story
        print(textfile)
        docFormatter.textProcess(textfile.replace('\n',''))
        print(os.getcwd())
        #os.chdir('')
        freqDict = modelGenerator.modelGenerator()
        driver.generateStory(freqDict)
        speechOutput.speechOutput()

        file = open('finalOutput.txt', 'r').readlines()

        for sentence in file:
            display_picture(sentence, app)
            text2Speech(sentence[1:-3])  # Reads the sentence outloud
            time.sleep(1)


root=Tk()
app=FullScreenApp(root)
root.mainloop()
#app.switch_picture(search_term)


'''
speech_subscription_key = '5c610c34de8646a0a455308e1082e1c4'

translator = Translator(speech_subscription_key)
output = translator.speak("This is a text to speech translation", "en-US", "Female", "riff-16khz-16bit-mono-pcm")
pygame.mixer.init()
pygame.mixer.music.load("file.wav")
pygame.mixer.music.play()
'''


#5c610c34de8646a0a455308e1082e1c4   bing text to speech

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
