from analysis_utils import get_all_event_id
from bs4 import BeautifulSoup
from filter_utils import *
soup = BeautifulSoup(open('output/broky.html'),'html.parser')
event_ids = get_all_event_id(soup)
print(event_ids)
url = "https://www.hltv.org/stats/players/events/15631/kscerato?startDate=2023-01-01&endDate=2023-12-31"
soup = soup = BeautifulSoup(open('output/KSCERATO.html'),'html.parser')
update = get_all_event_id(soup)
event_ids=list(set(event_ids+update))
url = "https://www.hltv.org/stats/players/events/15165/blamef?startDate=2023-01-01&endDate=2023-12-31"
soup = BeautifulSoup(open('output/blamef.html'),'html.parser')
update = get_all_event_id(soup)
event_ids=list(set(event_ids+update))
url='https://www.hltv.org/stats/players'
event_ids = ['6812', '7250', '7289', '6863', '7082', '6809', '7368', '6864', '7128', '6977', '6976', '6970', '7063', '6811', '6862', '7331', '7272', '6975', '6865', '6861', '7171', '6793', '6979', '6978', '6810', '7365', '7057', '6794', '7225', '6973', '7499', '6972', '6974']
for eid in event_ids:
    url = add_event_id(url,eid)
print(url)