#Main file

from crawler import crawl_web
from search import lucky_search, ordered_search


from crawler import crawl_web
from search import lucky_search, ordered_search

print "Please enter a seed page:"

seed = raw_input()

corpus = crawl_web(seed)

print "Index\n\n\n:"
print corpus.index
print "\n\n\n"

print "Graph:\n\n\n"
print corpus.graph
print "\n\n\n" 

print "Ranks:\n\n\n"
print corpus.ranks
print "\n\n\n"



