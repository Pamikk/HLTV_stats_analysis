def extract_fliters_from_url(url):
    tmp = url.split('&')
    tmp[0]=tmp[0].split('?')[-1]
    filters ={}
    for i in tmp:
        key,val=i.split('=')
        if key in filters.keys():
            filters[key].append(val)
        else:
            filters[key]=[val]
    return filters
def add_event_id(url,id):
    string = f'event={id}'
    if string in url:
        return url
    if '?' not in url:
        return url+f'?{string}'
    else:
        return url+f'&{string}'
def add_min_map(url,mmap):
    if '?' not in url:
        return f'{url}?minMapCount={mmap}'
    else:
        return f'{url}&minMapCount={mmap}'