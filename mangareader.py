from bs4 import BeautifulSoup as bs
import requests 
import cv2 
import numpy as np 

BASE_URL = "http://mangareader.net"

class Manga:
	def __init__(self,name,link=None,bolum=None):
		self.name = name
		self.link = link
		self.bolum = bolum
		if(self.link == None):
			self.link = self.get_link()
		if(self.bolum == None):
			self.bolum = self.get_last_chapter()	
	def get_link(self):
		manga_name = str(self.name).lower()
		link = BASE_URL + "/alphabetical"
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
	def get_last_chapter(self):
		#chico_manga
		link = BASE_URL + self.link
		page = requests.get(link).text
		soup = bs(page,'html.parser')
		linkler = soup.select("#latestchapters")
		#linkler = html_content.find_all(id="latestchapters")
		for element in linkler:
			text= element.find("li").find("a")
			if(len(text)>0):
				bolum = int(text.get("href").split('/')[2])
		return bolum

manga1 = Manga("Naruto")
print(manga1)