import requests
import os
from bs4 import BeautifulSoup
req = requests.get('https://maple.gg/u/%EB%A9%8D%EC%9D%80%EC%82%AC')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
basic_info = soup.select('.user-summary-item')

level = str(basic_info[0]).replace('<li class="user-summary-item">Lv.','').replace('</li>','')
level = level.split('(')[0]
popular = str(basic_info[2]).replace('<li class="user-summary-item"><span>인기도</span>\n<span>','').replace('</span></li>','')
mureung_floor = (str(soup.select('.user-summary-floor')[0]).replace('<h1 class="user-summary-floor font-weight-bold">',''))[:2]
mureung_time = str(soup.select('.user-summary-duration')[0]).replace('<small class="user-summary-duration">','').replace('</small>','')
ranking = soup.select('.user-additional > div')
guild = str(ranking[0]).replace('<div class="col-lg-2 col-md-4 col-sm-4 col-12 mt-3">\n<b class="d-inline-block d-sm-block">길드</b>\n','').replace('\n</div>','')
rank_world = str(ranking[2]).replace('<div class="col-lg-2 col-md-4 col-sm-4 col-6 mt-3">\n<b>월드랭킹</b><br/>\n<span>','').replace('</span>\n</div>','')
rank_world_job = str(ranking[3]).replace('<div class="col-lg-2 col-md-4 col-sm-4 col-6 mt-3">\n<b>직업랭킹(월드)</b><br/>\n<span>','').replace('</span>\n</div>','')
rank_job = str(ranking[4]).replace('<div class="col-lg-2 col-md-4 col-sm-4 col-6 mt-3">\n<b>직업랭킹(전체)</b><br/>\n<span>','').replace('</span>\n</div>','')
union_tier = str(soup.select('.user-summary-tier-string')[0]).replace('<div class="user-summary-tier-string font-weight-bold">','').replace('</div>','')
union_level = str(soup.select('.user-summary-level')[0]).replace('<span class="user-summary-level">Lv.','').replace('</span>','')

path = os.path.dirname(os.path.abspath(__file__))
if os.path.isfile(path + '/maungeunsa.js'):
    os.remove(path + '/maungeunsa.js')
datajs = open(path + '/maungeunsa.js', 'w', encoding='utf8')
data_str = 'var data = {\n\tlevel : "' + level + '",\n\tpopular : "' + popular + '",\n\tguild : ' + "'" + guild + "'" +',\n\tmureung_floor : "' + mureung_floor + '",\n\tmureung_time : "' + mureung_time + '",\n\trank_world : "' + rank_world + '",\n\trank_world_job : "' + rank_world_job + '",\n\trank_job : "' + rank_job + '",\n\tunion_tier : "' + union_tier + '",\n\tunion_level : "' + union_level + '"\n};'
datajs.write(data_str)
datajs.close()
