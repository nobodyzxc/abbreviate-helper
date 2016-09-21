#!/usr/bin/env python

import sys
import urllib2
from HTMLParser import HTMLParser

####################### SETTING ########################

if len(sys.argv) != 2:
    print "give me Only ONE parameter"
    quit()

word = sys.argv[1]

site = "https://www.allacronyms.com/" + word + "/abbreviated"

####################### ABBREV PAESER ##################
class abbParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.stopParse = False
        self.getDef = False
        self.lastTag = ""
    def handle_starttag(self , tag , attrs):
        self.lastTag = tag
        if not self.stopParse:
            if tag == "div":
                for(attr , value) in attrs:
                    if attr == 'class' and value == 'pairDef':
                        self.getDef = True
                    if attr == 'class' and value == 'abbreviated-separator':
                        self.stopParse = True
            if tag == "a" and self.getDef == True:
                for(attr , value) in attrs:
                    if attr == 'href':
                        print "%-7s" %value.split('/')[1] , " " , 
                        print "%-15s" %value.split('/')[2]
                        self.getDef = False
#######################    MAIN   ######################

if __name__ == '__main__':
    req = urllib2.Request(site)
    response = urllib2.urlopen(req)
    page = response.read() #Get html file
    RSP = abbParser()
    RSP.feed(page)
