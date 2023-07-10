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
