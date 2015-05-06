from twitter import *
import subprocess
import os

token = '' 
token_key = ''

con_secret = ''
con_secret_key = ''

t = Twitter(
    auth=OAuth(token, token_key, con_secret, con_secret_key))

##timeline = t.statuses.user_timeline(screen_name="autotroph1")

##print timeline[0]["text"]

timeline = t.search.tweets(q="#MIT")

print timeline ["statuses"][0]["text"]



##text2voice = timeline[0]["text"]
text2voice = timeline ["statuses"][0]["text"]

text2voice = text2voice.replace(" ", "+")

text2voice = text2voice.encode("ascii","ignore")
text2voice = text2voice.replace ("&amp;","and")

list_of = ['mplayer', '-ao','alsa', '-really-quiet','-noconsolecontrols'];
##url = 'http://translate.google.com/translate_tts?tl=en&q=' + text2voice
url = 'http://tts-api.com/tts.mp3?q=' + text2voice
list_of.append(url)

print list_of
subprocess.Popen(list_of)

##mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?tl=en&q=$*"; 
