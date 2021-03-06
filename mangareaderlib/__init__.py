from bs4 import BeautifulSoup as bs
import requests
from tqdm import tqdm
import json
import argparse


class Manga:
	def __init__(self, name, link, last_episode, img, desc, language, source):
		self.name = name
		self.link = link
		self.last_episode = last_episode
		self.img = img
		self.desc = desc
		self.language = language
		self.source = source

def mangareader():
	mangaReaderUpdates = []
	BASE_URL = "https://www.mangareader.net"
	link = BASE_URL + "/alphabetical"
	page = requests.get(link).text
	soup = bs(page, 'html.parser')

	linkler = soup.select(".series_alpha > li")
	for c,element in tqdm(enumerate(linkler),total=len(linkler)):
		manga_ismi= element.get_text()
		link = BASE_URL + element.find('a').get('href')
		if len(manga_ismi) > 1:
			page = requests.get(link).text
			soup = bs(page, 'html.parser')
			linkler = soup.select("#latestchapters")
			manga_img = soup.find("div", {"id" : "mangaimg"}).find("img").get("src")
			manga_desc = soup.select("div#readmangasum p")[0].text
			for element in linkler:
				try:
					text = element.find("li").find("a")
					if len(text) > 0:
						bolum = int(text.get("href").split('/')[2])
				except Exception:
					pass				
			mangaReaderUpdates.append(Manga(manga_ismi, link, bolum, manga_img, manga_desc, "eng", "mangareader"))
	return mangaReaderUpdates


def mangawt():
	mangaWTUpdates = []
	BASE_URL = "http://mangawt.com"
	manga_list = ["/manga-list?page=1","/manga-list?page=2"]
	for page_num in manga_list:
		link = BASE_URL + page_num	
		page = requests.get(link).text
		soup = bs(page, 'html.parser')
		linkler = soup.find_all('a', {"class": "chart-title"})
		for c, i in enumerate(tqdm(linkler, total=len(linkler))):
			link = i.get('href')
			manga_ismi = i.text
			if len(link) > 1:
				page = requests.get(link).text
				soup = bs(page, 'html.parser')
				manga_img = soup.find("img", {"class": "img-responsive"}).get("src")
				manga_desc = soup.select("div.well p")[0].text
				bolumler = soup.find('h5', {"class": "chapter-title-rtl"}).find('a').get('href')
				bolum = bolumler.split('/')[-1]
				mangaWTUpdates.append(Manga(manga_ismi, link, bolum, manga_img, manga_desc, "tr", "mangawt"))
		return mangaWTUpdates


def puzzmos():
	puzzMos = []
	# Aslında ana sayfada da yazıyor son bölüm ben bununla niye uğraştım ki -.-"
	BASE_URL = "https://puzzmos.com"
	manga_list = "/directory?Sayfa="
	# Maksimum sayfa numarasını çekmek için mantıklı bir çözüm düşüneceğim.
	for page_num in tqdm(range(1, 65)):
		link = BASE_URL + manga_list + str(page_num)
		req = requests.get(link).text
		soup = bs(req, 'html.parser')
		manga_linkleri = soup.find_all('h4', {"class": "media-heading"})
		for links in manga_linkleri:
			link = links.find('a').get('href')
			manga_ismi = links.find('a').text
			req = requests.get(link).text
			soup = bs(req, 'html.parser')
			manga_img = soup.find("img", {"class":"thumbnail"}).get("src")
			manga_desc = soup.select("div.col-md-9 p")[0].text.split("\n")[0]
			linkler = soup.find_all('table', {'class': 'table table-hover'})
			for link in linkler:
				if link.find('a') is not None:
					link = link.find('a').get('href')
					bolum = link.split('/')[-1]
					puzzMos.append(Manga(manga_ismi, link, bolum, manga_img, manga_desc, "tr", "puzzmos"))
	return puzzMos


def epikmanga():
	epikManga = []
	BASE_URL = "https://www.epikmanga.com"
	manga_list = "/seri-listesi"
	link = BASE_URL+manga_list
	req = requests.get(link).text
	soup = bs(req, 'html.parser')
	linkler = soup.find_all('h3', {'class': 'media-heading'})
	for c, link in enumerate(tqdm(linkler)):
		manga_ismi = link.text
		link = link.find('a').get('href')
		req = requests.get(link).text
		soup = bs(req, 'html.parser')
		linkler = soup.find('table', {'class': 'table table-bordered'}).find('a')
		manga_img = soup.find("img", {"class": "thumbnail"}).get("src")
		manga_desc = soup.select("div.col-md-12 p")[0].text.split("\n")[0]
		if linkler is not None:
			link = linkler.get('href')
			bolum = linkler.text[1:].split(" ")[0]
			str(manga_ismi).replace(":", "")
			epikManga.append(Manga(manga_ismi, link, bolum, manga_img, manga_desc, "tr", "epikmanga"))
	return epikManga


def mangakakalot():
	mangaKakalot = []
	BASE_URL = "http://mangakakalot.com"
	manga_list = "/manga_list?type=topview&category=all&state=all&page=" #max = 862
	for page_nums in tqdm(range(862)):
		link = BASE_URL + manga_list + str(page_nums)
		req = requests.get(link).text
		soup = bs(req, 'html.parser')
		linkler = soup.find_all('div', {'class':'list-truyen-item-wrap'})
		for link in linkler:
			if len(link) > 1:
				manga_ismi = link.find('a').get('title')
				link = link.find('a').get('href')
				req = requests.get(link).text
				soup = bs(req, 'html.parser')
				manga_img = soup.find("div", {"class": "manga-info-pic"}).find("img").get("src")
				manga_desc = soup.select("div#noidungm")[0].text.split("\n")[2]
				bolum = soup.find('div', {'class': 'chapter-list'}).find('a').get('href').split('_')[-1]
				mangaKakalot.append(Manga(manga_ismi, link, bolum, manga_img, manga_desc, "eng", "mangakakalot"))
	return mangaKakalot


def exportAsJSON(array, filename):
	with open(filename + ".json", "w+") as writer:
		writer.write("[")
		for x, manga in enumerate(array):
			writer.write(json.dumps(manga.__dict__, indent=4, ensure_ascii=False))
			if x != len(array)-1:
				writer.write(",")
		writer.write("]")


def main(args):
	try:
		exportAsJSON(globals()[args.s](), args.o)
	except Exception as err:
		print("Please check website again : " + str(err))
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Welcome to the mangareaderlibv1 i hope you like it", usage="python mangareaderlib.py --s [website] --o [outputfile]\nfor website you can choose : mangareader [eng] \nmangakakalot [eng] \npuzzmos[tr]\nepikmanga[tr]\nmangawt[tr] \nand you dont need to add .json for output file")
	parser.add_argument("--s", help="select which source you want to scrap? You can check from github page")
	parser.add_argument("--o", help="output json file's name", default="output")
	args = parser.parse_args()
	main(args)