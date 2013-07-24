def get_all_links(page):
    #INPUT: page-url
    #OUTPUT: list of links on page
    html = get_page(page)
    print 'Website loaded: ' + page
    arrLinks = []

    while True:
        url, endpos = get_next_target(html)

        if (url):
            arrLinks.append(url)
            html = html[endpos:]
        else:
            break

    return arrLinks



def get_next_target(html):
    #INPUT: html of a website
    #OUTPUT: URL and current search position in the HTML-string
    start_link = html.find(' <a href="/gjc-cgi/listjobs.pl?order=title">title</a')

    if (start_link == -1):
        return None, -1
    else:  
        start_quote = html.find('"', start_link + 1)
        end_quote = html.find('"', start_quote + 1)
        url = html[start_quote + 1:end_quote]

        return url, end_quote + 1



def crawl(seed_page):
    #INPUT: URL of the seed-page
    #OUTPUT: list of URLs of all crawled pages
    tocrawl = [seed_page]
    crawled = []

    while (len(tocrawl) > 0):
        #print 'Pages to crawl: '
        #print tocrawl

        page = tocrawl.pop()
        print 'Now crawling: ' + page

        new_links = get_all_links(page)

        crawled.append(page)

        for link in new_links:
            if link not in crawled:
                tocrawl.append(link)

        print 'New Links: '
        print new_links
        print'---'

    return crawled



def get_page(url):
    #INPUT: URL of any website
    #OUTPUT: HTML-string of the website
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""


#TESTCODE STARTS HERE
var = raw_input('Enter Website: ')
seed_page = var
seed_html = get_page(seed_page)   
print 'Seed-Page: ' + seed_page
print '==============================='
print 'Seed-HTML: '
print seed_html
print '==============================='
print 'Links on Seed-Page: '
print get_all_links(seed_page)
print '==============================='
print '==============================='
print 'Crawling started...'
found_urls = crawl(seed_page)
print 'Crawling done!'
print '==============================='
print '==============================='
print 'All links crawled: '
print found_urls
print '==============================='
