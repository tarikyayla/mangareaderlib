from bs4 import BeautifulSoup as bs
import requests
import cv2
import numpy as np
from tqdm import tqdm
import json



class Manga:
	def __init__(self, name, link=None, source=None, last_chapter=None, lang=None,
				 mangaimg=None, description=None):
		self.name = name
		self.link = link
		self.source = source
		self.last_chapter = last_chapter
		self.lang = lang


class Chapter(Manga):
	def __init__(self, name, link, source, chapter, lang):
		self.name = name
		self.link = link
		self.source = source
		self.chapter = chapter
		self.lang = lang


class Website:
	def __init__(self):
		pass

	def mangareader(self):
		obj = Mangareader()
		return obj


class Mangareader(Website):
	def __init__(self):
		pass

	@classmethod
	def updateAll(self):
		mangaReaderUpdates = []
		BASE_URL = "https://www.mangareader.net"
		link = BASE_URL + "/alphabetical"
		page = requests.get(link).text
		soup = bs(page, 'html.parser')
		#linkler = soup.find_all("div",{"class": "series_col"})
		linkler = soup.select(".series_alpha > li")
		for c, element in tqdm(enumerate(linkler[:20]), total=20):
			manga_ismi = element.get_text()
			link = BASE_URL + element.find('a').get('href')
			if len(manga_ismi) > 1:
				page = requests.get(link).text
				soup = bs(page, 'html.parser')
				linkler = soup.select("#latestchapters")
				#linkler = html_content.find_all(id="latestchapters")
				for element in linkler:
					text = element.find("li").find("a")
					if(len(text) > 0):
						bolum = int(text.get("href").split('/')[2])
				# print(manga_ismi,link,bolum)
				mangaReaderUpdates.append(
					Chapter(manga_ismi, link, "mangareader", bolum, "eng"))
		return mangaReaderUpdates

	@classmethod
	def list_all(self):
		pass


def exportAsJSON(array, filename):
	with open(filename + ".json", "w+") as writer:
		writer.write("[")
		for x, manga in enumerate(array):
			writer.write(json.dumps(manga.__dict__, indent=4, ensure_ascii=False))
			if(x != len(array)-1): writer.write(",")
		writer.write("]")


website = Website()
