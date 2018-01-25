def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        pagelink = tocrawl.pop()
        if pagelink not in crawled:
            content = get_page(pagelink)
            add_page_to_index(index, pagelink, content)
            union(tocrawl, get_all_links(content))
            crawled.append(pagelink)
    return index