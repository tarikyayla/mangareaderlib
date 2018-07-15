from bs4 import BeautifulSoup as bs
import requests 
import cv2 
import numpy as np 

BASE_URL = "http://mangareader.net/"

class Manga:
	def __init__(self,name):
		self.name = name
		self.link = self.search_for_link()
	def search_for_link(self):
		manga_name = str(self.name).lower()
		link = BASE_URL + "alphabetical"
		page = requests.get(link).text
		soup = bs(page, 'html.parser')
		linkler = soup.select(".series_alpha > li")
		for element in linkler:
			text= element.get_text().lower()
			if len(text) > 1 :
				text = text.replace("'","")
			if manga_name == text:
				link = element.find('a').get('href')
		return link
		
manga1 = Manga("Naruto")
print(manga1.link)