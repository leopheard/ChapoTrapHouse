from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon
import requests
import re
from bs4 import BeautifulSoup

plugin = Plugin()

URL = "https://feeds.soundcloud.com/users/soundcloud:users:211911700/sounds.rss"

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://i1.sndcdn.com/avatars-000230770726-ib4tc4-t500x500.jpg"},
   {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://i1.sndcdn.com/avatars-000230770726-ib4tc4-t500x500.jpg"},
    ]

    return items

@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL)
    
    playable_podcast = mainaddon.get_playable_podcast(soup)
    
    items = mainaddon.compile_playable_podcast(playable_podcast)

    return items


@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items


if __name__ == '__main__':
    plugin.run()
