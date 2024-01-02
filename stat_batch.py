import re
import time
from tqdm import tqdm
from filter_utils import *
from web_utils import *
from analysis_utils import *
from utils import *

url='https://www.hltv.org/stats/players?event=6979&event=6812&event=7250&event=7289&event=6863&event=7082&event=6809&event=6864&event=7128&event=6977&event=6976&event=6970&event=6811&event=6862&event=6975&event=6865&event=6861&event=6793&event=6978&event=6810&event=7365&event=6794&event=6973&event=7499&event=6972&event=6974&event=6971'

#url = add_min_map(url,60)
soup = get_html_url_curlc(url)
players_links = []
for item in soup.find_all('a'):
    item_cls = item.get('class')
    
    if test_ignore(item_cls):
        continue
    link = item.get('href')
    if link is None:
          continue
    m1 = re.search(r'players\/\d',link)
    if m1!=None:
        players_links.append(link)
print(len(players_links))
player_stats=[]
host_url = 'https://www.hltv.org'
val_func = lambda x: float(x['Rating 2.0'])*100+float(x['K/D Ratio'])/10.0
for link in tqdm(players_links):
    r_player = get_html_url_curlc(host_url+link)
    #print('get data')
    text = r_player.get_text()
    text = text.split('\n')
    tmp = []
    for line in text:
        line = line.strip()
        if len(line)>0:
            tmp.append(line)
    text = tmp
    res = get_player_stats(text)
    if res not in player_stats:
        player_stats.append(res)
    time.sleep(0.5)

#player_stats.sort(key= val_func,reverse=True)
save_dict_to_csv('./data/rating_2023',player_stats)