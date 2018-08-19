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
			mangaReaderUpdates.append([manga_ismi,link,bolum])
	return mangaReaderUpdates

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

def mangaUpdatesfromPuzzmos():
	puzzMos = []
	# Aslında ana sayfada da yazıyor son bölüm ben bununla niye uğraştım ki -.-"
	BASE_URL = "https://puzzmos.com"
	manga_list = "/directory?Sayfa="
	# Maksimum sayfa numarasını çekmek için mantıklı bir çözüm düşüneceğim.
	for page_num in tqdm(range(1,65)):
		link = BASE_URL + manga_list + str(page_num)
		req = requests.get(link).text
		soup = bs(req,'html.parser')
		manga_linkleri = soup.find_all('h4',{"class":"media-heading"})
		for links in manga_linkleri:
			link = links.find('a').get('href')
			manga_ismi = links.find('a').text
			req = requests.get(link).text
			soup = bs(req,'html.parser')
			linkler = soup.find_all('table',{'class':'table table-hover'})
			for link in linkler:
				if(link.find('a') != None): 
					link = link.find('a').get('href')
					episode = link.split('/')[-1]
					puzzMos.append([manga_ismi,link,episode])
	return puzzMos

def mangaUpdatesFromEpikManga():
	epikManga = []
	BASE_URL = "https://www.epikmanga.com"
	manga_list = "/seri-listesi"
	link = BASE_URL+manga_list
	req = requests.get(link).text
	soup = bs(req,'html.parser')
	linkler = soup.find_all('h3',{'class':'media-heading'})
	for c,link in enumerate(tqdm(linkler[:15])):
		manga_ismi = link.text
		link = link.find('a').get('href')
		req = requests.get(link).text
		soup = bs(req,'html.parser')
		linkler = soup.find('table',{'class':'table table-bordered'}).find('a')
		if(linkler != None):
			link = linkler.get('href')
			bolum = linkler.text[1:].split(" ")[0]
			str(manga_ismi).replace(":","")
			mangaObject = mangareader.Manga(manga_ismi,link,bolum)
			#epikManga.append([manga_ismi,link,bolum])
			epikManga.append(mangaObject)
	return epikManga

def mangaUpdatesFromMangaKakalot():
	mangaKakalot = []
	BASE_URL = "http://mangakakalot.com"
	manga_list = "/manga_list?type=topview&category=all&state=all&page=" #max = 862
	for page_nums in tqdm(range(1)):
		link = BASE_URL + manga_list + str(page_nums)
		req = requests.get(link).text
		soup = bs(req,'html.parser')
		linkler = soup.find_all('div',{'class':'list-truyen-item-wrap'})
		for link in linkler:
			if(len(link)>1):
				manga_ismi = link.find('a').get('title')
				link = link.find('a').get('href')
				req = requests.get(link).text
				soup = bs(req,'html.parser')
				bolum = soup.find('div',{'class':'chapter-list'}).find('a').get('href').split('_')[-1]
				mangaKakalot.append([manga_ismi,link,bolum])
	return mangaKakalot

