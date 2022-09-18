from bs4 import BeautifulSoup
import requests as re

print('''
    _        _           _  __    
   /_\  _ _ (_)_ __  ___| |/ /  _ 
  / _ \| ' \| | '  \/ -_) ' < || |
 /_/ \_\_||_|_|_|_|_\___|_|\_\_,_|

Script by ibrahKrep
''')
try:
  anime_s = input('Masukkan Judul Anime: ')
  data = re.get('https://otakudesu.video/', params={'s': {anime_s}, 'post_type': 'anime'}).text
  soup = BeautifulSoup(data, 'lxml')
  anime = soup.find('ul', class_='chivsrc')
  anime_link = anime.li.h2.a['href']
  anime_info = re.get(anime_link).text
  soup2 = BeautifulSoup(anime_info, 'lxml')
  anime_ilist = soup2.find('div', class_='venser').find('div', class_='fotoanime').find('div', class_='infozin').find('div', class_='infozingle').find_all('p')
  anime_list = soup2.find('div', class_='episodelist')
  anime_bdlink = anime_list.ul.li.span.a['href']
  anime_binfo = re.get(anime_bdlink).text
  soup3 = BeautifulSoup(anime_binfo, 'lxml')
  batch = soup3.find('div', class_='batchlink')
  batch_link = batch.ul.li.a['href']

  print(f'''
  [!] Server otakudesu

  {anime_ilist[0].text}
  {anime_ilist[2].text}
  {anime_ilist[3].text}
  {anime_ilist[4].text}
  {anime_ilist[5].text}
  {anime_ilist[6].text}
  {anime_ilist[7].text}
  {anime_ilist[8].text}
  {anime_ilist[9].text}
  {anime_ilist[10].text}


  Download Batch: {batch_link}

  ''')
except:
	print('Not found!')
