import csv
from collections import namedtuple
from os.path import isfile
from threading import Thread
from time import sleep, ctime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BANDCAMP_URL = 'https://bandcamp.com/'

TrackRec = namedtuple('TrackRec',
                     ['title',
                      'artist',
                      'artist_url',
                      'album',
                      'album_url',
                      'timestamp'   # when you played it
                     ])



class BandLeader():

    def __init__(self, csvpath=None):
        self.database_path = csvpath
        self.database = []

        if isfile(self.database_path):
            with open(self.database_path, 'r') as dbfile:
                dbreader = csv.reader(dbfile)
                next(dbreader)  # skip header
                self.database = [TrackRec(*row) for row in dbreader]

        self.browser = webdriver.Chrome()
        opts = Options()
        opts.add_argument('--headless')
        self.browser.get(BANDCAMP_URL)

        self._current_track_number = 1
        self.track_list = []
        self.tracks()

        self._current_track_record = None

        self.thread = Thread(target=self._maintain)
        self.thread.daemon = True
        self.thread.start()
        self.tracks()

    def _maintain(self):
        self._update_db()
        sleep(20)

    def save_db(self):
        with open(self.database_path, 'w', newline='') as dbfile:
            dbwriter = csv.writer(dbfile)
            dbwriter.writerow(list(TrackRec._fields))
            for entry in self.database:
                dbwriter.writerow(list(entry))

    def _update_db(self):
        try:
            check = (self._current_track_record is not None
                     and (len(self.database) == 0
                          or self.database[-1] != self._current_track_record)
                     and self.is_playing())
            if check:
                self.database.append(self._current_track_record)
                self.save_db()
        except Exception as e:
            print('error while updating the db: {}'.format(e))

    def is_playing(self):
        playbtn = self.browser.find_element(By.CLASS_NAME, 'playbutton')
        return playbtn.get_attribute('class').find('playing') > -1

    def currently_playing(self):

        try:
            if self.is_playing():
                title = self.browser.find_element(By.CLASS_NAME,'title').text
                album_detail = self.browser.find_element(By.CSS_SELECTOR,'.detail-album > a')
                album_title = album_detail.text
                album_url = album_detail.get_attribute('href').split('?')[0]
                artist_detail = self.browser.find_element(By.CSS_SELECTOR,'.detail-artist > a')
                artist = artist_detail.text
                artist_url = artist_detail.get_attribute('href').split('?')[0]
                return TrackRec(title, artist, artist_url, album_title, album_url, ctime())
        except Exception as e:
            print('there was an error: {}'.format(e))

        return None

    def tracks(self):
        sleep(1)
        discover_section = self.browser.find_element(By.CLASS_NAME, 'discover-results')
        left_x = discover_section.location['x']
        right_x = left_x + discover_section.size['width']

        discover_items = self.browser.find_elements(By.CLASS_NAME, 'discover-item')
        self.track_list = [t for t in discover_items if left_x <= t.location['x'] < right_x]

        for (i, track) in enumerate(self.track_list):
            print(f'{i + 1}')
            lines = track.text.split('\n')
            print(f'Album: {lines[0]}')
            print(f'Artist: {lines[1]}')
            if len(lines) > 2:
                print(f'Genre: {lines[2]}')

    def more_tracks(self, page='next'):
        next_btn = [e for e in self.browser.find_elements(By.CLASS_NAME, 'item-page')
                    if e.text.lower().strip() == str(page)]
        if next_btn:
            next_btn[0].click()
            self.tracks()

    def play(self, track=None):
        if track is None:
            self.browser.find_element(By.CLASS_NAME, 'playbutton').click()
        elif type(track) is int and len(self.track_list) >= track >= 1:
            self._current_track_number = track
            self.track_list[self._current_track_number - 1].click()

        sleep(1)
        if self.is_playing():
            self._current_track_record = self.currently_playing()

    def play_next(self):
        if self._current_track_number < len(self.track_list):
            self.play(self._current_track_number + 1)
        else:
            self.more_tracks()
            self.play(1)


    def pause(self):
        self.play()

if __name__ == '__main__':
    t = BandLeader('test.csv')
    t.play(1)