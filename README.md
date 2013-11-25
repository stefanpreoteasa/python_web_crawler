python_web_crawler
==================

Basic web crawler. Based on Udacity CS101 final project.

Takes a website string as input and then crawls the web starting from that initial seed page.

Stops after having crawled 100 pages. I will probably change this to a user input decision in the next version.

Returns a WebCorpus object and prints out:

1. An index 
2. A graph of websites and their relationships to each other
3. A list of the websites in the graph and how 'linked to' they are. A page with more links will have a higher rank.

