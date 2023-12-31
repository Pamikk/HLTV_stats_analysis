from requests_html import HTMLSession
import re
import time
from tqdm import tqdm
import csv

def add_event_id(url,id):
    string = f'event={id}'
    if string in url:
        return url
    if '?' not in url:
        return url+f'?{string}'
    else:
        return url+f'&{string}'
def get_stat_from_form(player,text):
    text = text.strip()
    m = re.search(r"\d", text)
    idx = m.span()[0]
    key = text[:idx].strip()
    player[key] = text[idx:]
def get_player_stats(player_url):
    try:
        url_head ='https://www.hltv.org'
        r_player = session.get(url_head+player_url)
        #print('get data')
        text = r_player.html.text
        print(text)
        text = text.split('\n')
        player = {'id':text[86],'Rating 2.0':text[95],'Surviving':1-float(text[101]),'KAST':text[107],'IMPACT':text[113],'ADR':text[119],'KPR':text[125]}

        #print('Deal with stats with form, can be redundant')
        for i in range(129,143):
            if 'Rating' in text[i]:
                continue
            get_stat_from_form(player,text[i])
        #print('update rating against top team')
        for i in range(144,156,3):
            key = text[i+1].strip()
            player[f'Rating {key}'] = text[i]
            player[f'#Maps {key}'] = text[i+2].strip()[1:-1].split()[0]
        return player
    except:
        print('error',player_url)
        return None
def save_dict_to_csv(name,data):    
    with open(f'{name}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(data[0].keys()))
        writer.writeheader()
        writer.writerows(data)
session = HTMLSession()
def add_min_map(url,mmap):
    if '?' not in url:
        return f'{url}?minMapCount={mmap}'
    else:
        return f'{url}&minMapCount={mmap}'
    
event_ids = []#[6477,6349,6348,6586,6141,6346,6140,6345,6138,6372,6137,6136,6343,6503,6384,6219,6588,6510,6714,6713,6381,6382,6334,6347,6344]#6334,6477
url='https://www.hltv.org/stats/players'
for eid in event_ids:
    url = add_event_id(url,eid)
#url = add_min_map(url,60)
print(url)

r = session.get(url)
links = r.html.links
players_links = []
print(players_links)
for link in links:
    m1 = re.search(r'players\/\d',link)
    if m1!=None:
        if 'teamId' not in link:        
            players_links.append(link)
player_stats=[]
val_func = lambda x: float(x['Rating 2.0'])*100+float(x['K/D Ratio'])/10.0
for link in tqdm(players_links):
    res = get_player_stats(link)
    print(res)
    exit()
    if res!=None:
        player_stats.append(res)
    time.sleep(0.5) #avoid being banned from HLTV

player_stats.sort(key= val_func,reverse=True)
save_dict_to_csv('rating_2022',player_stats)