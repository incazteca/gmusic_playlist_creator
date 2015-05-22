import os
import json
import sys

from gmusicapi import Mobileclient

with open('../config/login.json') as data_file:
    credentials = json.load(data_file)

# Retrieve input file
print str(sys.argv)
print str(credentials)

song_list = sys.argv[1]

api = Mobileclient()
api.login(credentials['login'], credentials['password'])

with open(song_list) as input_file:
    for line in input_file:
        if line[0] == '#' or line == '\n':
            continue
        else:
            line = line.rstrip('\n')
            song, artist, option = line.split('|')
            song = song.strip()
            artist = artist.strip()
            option = option.strip()

            # Begin searching



