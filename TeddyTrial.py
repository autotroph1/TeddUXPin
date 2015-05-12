from twitter import *
import subprocess
import os
import re
import time

token = ''
token_key = ''

con_secret = ''
con_secret_key = ''

t = Twitter(
    auth=OAuth(token, token_key, con_secret, con_secret_key))

## Debug print time line of user
##timeline = t.statuses.user_timeline(screen_name="autotroph1")
##print timeline[0]["text"]

## using twitter API
timeline = t.search.tweets(q="#MIT")

## debug
## print timeline ["statuses"][0]["text"]

old_id = 0

while(True):
    sound_cmd =['mplayer', '-ao','alsa', '-really-quiet','-noconsolecontrols']
    url = 'http://tts-api.com/tts.mp3?q='
    timeline = t.statuses.user_timeline(screen_name="autotroph1")
    ##timeline = t.search.tweets(q="#MIT")
    ##tweet_id = timeline["statuses"][0]["text"]
    tweet_id = timeline[0]["id"]
    if (old_id != tweet_id):
        old_id = tweet_id
        ##text2voice = timeline[0]["text"]
        ##text2voice = timeline ["statuses"][0]["text"]
        text2voice =timeline[0]["text"]
        # encode unicode to ascii
        text2voice = text2voice.encode("ascii","ignore").rstrip()
        # conver & to and
        text2voice = text2voice.replace ("&amp;","and")
        # conver # to hash tag
        text2voice = text2voice.replace ("#", " hash tag ")
        print text2voice
        # remove any HTML stuff
        text2voice = re.sub(r'https?:\/\/[\n\r\S]*', '', text2voice, flags=re.MULTILINE)
        #remove all spcae
        text2voice = text2voice.replace(" ", "+")


        #debug print the url
        url = url + text2voice
        sound_cmd.append(url)
        ##print 'start motor'
        ##print(sound_cmd)
        ##url = 'http://translate.google.com/translate_tts?tl=en&q=' + text2voice
        motorP = subprocess.Popen(['python','motor.py'])
        soundP = subprocess.Popen(sound_cmd)
        soundP.wait()
        motorP.kill()
        ##print 'stor motor'
        ##mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?tl=en&q=$*";
        time.sleep(60)
