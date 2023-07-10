from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

BANDCAMP_URL = 'https://bandcamp.com/'


class BandLeader():
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get(BANDCAMP_URL)

        self._current_track_number = 1
        self.track_list = []
        self.tracks()

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
        elif type(track) is int and track <= len(self.track_list) and track >= 1:
            self._current_track_number = track
            self.track_list[self._current_track_number - 1].click()

    def play_ext(self):
        if self._current_track_number < len(self.track_list):
            self.play(self._current_track_number + 1)
        else:
            self.more_tracks()
            self.play(1)


    def pause(self):
        self.play()
