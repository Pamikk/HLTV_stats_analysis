import requests
import bs4
hltv_stats = "https://www.hltv.org/stats"
hltv_filters = {'side':['COUNTER_TERRORIST','TERRORIST'],'startDate':['2023-08-18'],'endDate':['2023-11-1']}
def batch_get_players(filters=None):
    web = hltv_stats+'/players'
    

