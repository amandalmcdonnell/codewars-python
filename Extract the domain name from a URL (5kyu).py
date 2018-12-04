def domain_name(url):
    if url.find('//')>0:
        return url[(url.find('//')+2) : url.find('.')]
    else:
        url=url[url.index('.')+1:]
        return url[:url.index('.')]
