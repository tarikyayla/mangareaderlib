from bs4 import BeautifulSoup as bs
import requests
from tqdm import tqdm

# Mangareader: 

def mangaUpdatesFromMangaReader():
	mangaReaderUpdates = []
	BASE_URL = "https://www.mangareader.net"
	link = BASE_URL + "/alphabetical"
	page = requests.get(link).text
	soup = bs(page, 'html.parser')
	#linkler = soup.find_all("div",{"class": "series_col"})
	linkler = soup.select(".series_alpha > li")
	for c,element in tqdm(enumerate(linkler),total=len(linkler)):
		manga_ismi= element.get_text()
		link = BASE_URL + element.find('a').get('href')
		if len(manga_ismi) > 1 :
			page = requests.get(link).text
			soup = bs(page,'html.parser')
			linkler = soup.select("#latestchapters")
			#linkler = html_content.find_all(id="latestchapters")
			for element in linkler:
				text= element.find("li").find("a")
				if(len(text)>0):
					bolum = int(text.get("href").split('/')[2])
			#print(manga_ismi,link,bolum)
			mangaReaderUpdates.append(manga_ismi,link,bolum)
	return mangaReaderUpdates

"""
def mangaVadisiUpdates:
	#class = media-heading
	BASE_URL = "http://manga-v2.mangavadisi.org"
	manga_list = ["/manga-list?page=1","/manga-list?page=2"]


"""

def mangaWTUpdates():
	mangaWTUpdates = []
	#class = chart-title
	BASE_URL = "http://mangawt.com"
	manga_list = ["/manga-list?page=1","/manga-list?page=2"]
	for page_num in manga_list:
		link = BASE_URL + page_num	
		page = requests.get(link).text
		soup = bs(page,'html.parser')
		linkler = soup.find_all('a',{"class": "chart-title"})
		for c,i in enumerate(tqdm(linkler,total=len(linkler))):
			link = i.get('href')
			manga_ismi = i.text
			if(len(link)>1):

				page = requests.get(link).text
				soup = bs(page,'html.parser')
				bolumler = soup.find('h5',{"class":"chapter-title-rtl"}).find('a').get('href')
				# bolumler = soup.select(".chapter-title-rtl > a")
				# children = bolumler.findChildren("a" , recursive=False)
				# for child in children:
				# 	print(chil.get('href'))
				bolum = bolumler.split('/')[-1]
				mangaWTUpdates.append([manga_ismi,link,bolum])
		return mangaWTUpdates

print(mangaWTUpdates())