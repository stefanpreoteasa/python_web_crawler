
import urllib2

#crawler uses this function, not the old one further down
def real_get_page(url):
    try:
        return urllib2.urlopen(url).read()
    except:
        return ""



def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print "Page not in cache: " + url
        return None
    
def make_cache(seed):
    tocrawl = [seed]
    crawled = []
    graph = {seed: []}
    index = {}
    print "cache = {"
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            ## print "Crawing: " + page
            content = real_get_page(page)
            print "   '" + page + "'" + ': """' + content + '""", '
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            for link in outlinks:
                if link in graph: # already found one link to it
                    graph[link].append(page)
                else:
                    graph[link] = [page]
            union(tocrawl, outlinks)
            crawled.append(page)
    print "}"


    
