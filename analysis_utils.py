import re
from filter_utils import *
def get_all_event_id(soup):
	event_ids=[]
	for link in soup.find_all('a'):
		event_link = link.get('href')
		if event_link == None:
			continue
		if '&event'in event_link:
			filters = extract_fliters_from_url(event_link)
			event_ids+=filters['event']
	return event_ids
def get_stat_from_form(player,text):
    text = text.strip()
    m = re.search(r"\d", text)
    idx = m.span()[0]
    key = text[:idx].strip()
    player[key] = text[idx:]
def get_player_stats(text):
    #text = text.split('\n')
    player = {'id':text[91],'Rating 2.0':text[99],'Surviving':1-float(text[104]),'KAST':text[109],'IMPACT':text[114],'ADR':text[119],'KPR':text[124]}
    

    #print('Deal with stats with form, can be redundant')
    for i in range(128,142):
        if 'Rating' in text[i]:
            continue
        get_stat_from_form(player,text[i])
    #print('update rating against top team')
    for i in range(143,155,3):
        key = text[i+1].strip()
        player[f'Rating {key}'] = text[i]
        player[f'#Maps {key}'] = text[i+2].strip()[1:-1].split()[0]
    return player
