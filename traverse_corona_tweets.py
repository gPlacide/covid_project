import os
import zipfile
import csv 
import json
import glob
import gzip
import json
import datetime
import demoji
import re
import pandas as pd 
import emoji


def format_line(line):
    line = demoji.replace(line)
    line = re.sub(r"(@\S*)", "@", line)
    line = re.sub(r"https://\S*", "url",line)
    return line


def text_has_emoji(text):
    for character in text:
        if character in emoji.UNICODE_EMOJI:
            return True
    return False

lst_lines = []
datadir = '/data-fast/corona_tweets/'
directory = glob.glob('/data-fast/corona_tweets/geoTwitter20-05-11.zip.gz')

lst_dates = []
lst_counts = []

lst_masks = []
lst_ids = []
lst_text = []
count_total = 0
count_english = 0
count_emojis = 0
for filename in sorted(directory):
    with gzip.open(filename, 'rb') as f:
        name  = os.path.basename(filename)
        name = name[:-7]
        name = name[10:]
        name = "20" + name
        date1 = datetime.datetime.strptime(name, "%Y-%m-%d")
        print(date1)
        count_day = 0 
        for line in f:
            tweet = json.loads(line)
            print(tweet['text'])
            count_total = count_total+1
            if tweet['lang'] == 'en':
                count_english = count_english+ 1
            if text_has_emoji(tweet['text']):
                count_emojis =count_emojis+1

#print("total emojis = " , count_emojis)
#print("total english = " ,count_english)
#print("total count = ",count_total)
        