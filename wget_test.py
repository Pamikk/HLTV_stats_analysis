import os
ua = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
import sys
def do_system(arg):
	print(f"==== running: {arg}")
	err = os.system(arg)
	if err:
		print("FATAL: command failed")
		sys.exit(err)
def get_html_url_wget(url,save_path='./data',save_name=None,keep=False):
	save_name='tmp.html' if save_name is None else save_name
	tgt_name = os.path.join(save_path,save_name)
	do_system(f'wget --user-agent={ua} {url} -O')