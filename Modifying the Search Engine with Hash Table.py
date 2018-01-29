def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = {}
    while tocrawl:
        pagelink = tocrawl.pop()
        if pagelink not in crawled:
            content = get_page(pagelink)
            add_page_to_index(index, pagelink, content)
            union(tocrawl, get_all_links(content))
            crawled.append(pagelink)
    return index

def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    return index[kewyord] if keyword in index else None
    
def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
                     
def get_page(pagelink):
    try:
        import urllib
        return urllib.open(pagelink).read()
    except:
        return ""