from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import Firefox
import urllib.request
import random
import json
import time
import sys
import os
import re

def dorking(browser, search_term):
	root = 'https://duckduckgo.com'
	q = f'{root}/?t=ffab&q={search_term.replace(" ","+")}&ia=web'
	browser.get(q)
	print(search_term)
	input('Ready to spider?')
	links = pull_links(browser.page_source,'https://')
	blacklist = ['gstatic','google']
	for page in links:
		if page.find('gtsatic')<0 and page.find('google')<0:
			print(f'Searching {page}')
			browser.get(f'https://{page}')
			time.sleep(10)
		else:
			break

def get_browser():
	options = Options()
	profile = FirefoxProfile()
	profile.set_preference("javascript.enabled", True)
	options.profile = profile 
	return Firefox(options)


def pull_links(html, delim):
	links = []
	for i in re.finditer(delim, html):
		ind = i.start()
		link = html[ind+len(delim):].split('"')[0]
		links.append(link)
	return links


def random_sleep(maxdt):
	delay = random.randint(1, maxdt)
	time.sleep(delay)
	return


dorking(get_browser(),'inurl: pdf')