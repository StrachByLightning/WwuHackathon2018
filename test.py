import pyttsx3

from flickrapi import FlickrAPI

FLICKR_PUBLIC = '6fdf088b862a49a3ae1e678296c00936'
FLICKR_SECRET = '605ede6b9004a09e'

flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
extras='url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
cats = flickr.photos.search(text='grass', per_page=5, extras=extras)
photos = cats['photos']
from pprint import pprint
pprint(photos)
"""

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
