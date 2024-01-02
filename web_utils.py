import requests
from bs4 import BeautifulSoup
import os
import subprocess
ua = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
hltv_stats = "https://www.hltv.org/stats"
hltv_filters = {'side':['COUNTER_TERRORIST','TERRORIST'],'startDate':['2023-08-18'],'endDate':['2023-11-1']}
def batch_get_players(filters=None):
    web = hltv_stats+'/players'
    
def get_html_url_wget(url,save_path='./output',save_name=None,keep=False):
	save_name='tmp.html' if save_name is None else save_name
	tgt_name = os.path.join(save_path,save_name)
	subprocess.run(['wget','--user-agent',ua,'-O',tgt_name,url])
	soup = BeautifulSoup(open(tgt_name), 'html.parser')
	if not keep:
		os.remove(tgt_name)
		
	return soup
def get_html_url_curlc(url,save_path='./output',save_name=None,keep=False):
	save_name='tmp.html' if save_name is None else save_name
	tgt_name = os.path.join(save_path,save_name)
	subprocess.run(['curl_chrome104','-s','-o',tgt_name,'--url', url])
	soup = BeautifulSoup(open(tgt_name), 'html.parser')
		
	return soup
