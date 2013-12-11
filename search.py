
### search.py




def lookup(windex, keyword):
    if keyword in windex.index:
        return windex.index[keyword]
    else:
        return None

def lucky_search(windex, keyword):
    #"I am feeling lucky" type algorithm
    #returns page with highest rating
    pages = lookup(windex, keyword)
    if not pages:
        return None
    best_page = pages[0]
    for candidate in pages:
        if windex.ranks[candidate] > windex.ranks[best_page]:
                best_page = candidate
    return best_page

def quicksort_pages(pages, ranks):
    #recursive sorting algorithm
    if not pages or len(pages) <= 1:
        return pages
    else:
        pivot = ranks[pages[0]]
        worse = []
        better = []
        for page in pages[1:]:
            if ranks[page] <= pivot:
                worse.append(page)
            else:
                better.append(page)
        return quicksort_pages(better, ranks) + [pages[0]] + quicksort_pages(worse, ranks)
            
def ordered_search(windex, keyword):
    pages = windex.lookup(keyword)
    return quicksort_pages(pages, windex.ranks)
