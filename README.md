# mangareaderlib

With this python module you can scrap manga sites and export as json. You can check all updated json files in json folder.

###### ***Currently supporting python 3.5+***

# Installation
    pip install git+https://github.com/tarikyayla/mangareaderlib
**or**
```shell
git clone https://github.com/tarikyayla/mangareaderlib
cd mangareaderlib
python setup.py install
```
# Usage

```python
import mangareaderlib as mr 
# mr.exportAsJSON(mangaArray,Outpufile)
mr.exportAsJSON(mr.epikmanga(),'epikmanga')
mr.exportAsJSON(mr.mangareader(),'mangareader')
mr.exportAsJSON(mr.mangakakalot(),'mangakakalot')
mr.exportAsJSON(mr.puzzmos(),'puzzmos')
mr.exportAsJSON(mr.mangawt(),'mangawt')
# if you want to edit script just type print(mr.__file__) and open with editor.
```

# Site List

| Status | Websites | Language | 
| -------- | -------- | -------- |
| <ul><li>- [x] Works</li></ul> | https://puzzmos.com/ | Turkish | 
| <ul><li>- [x] Works</li></ul> | http://mangawt.com   | Turkish |
| <ul><li>- [x] Works</li></ul> | https://www.epikmanga.com | Turkish |
| <ul><li>- [ ] Works</li></ul> | https://mangacim.com/ | Turkish |
| <ul><li>- [x] Works</li></ul> | http://mangareader.net | English |
| <ul><li>- [x] Works</li></ul> | http://mangakakalot.com/ | English |
| <ul><li>- [ ] Works</li></ul> | https://mangarock.com/ | English |
