# Library for opening url and creating
# requests
import urllib.request
import numpy as np
 
# pretty-print python data structures
from pprint import pprint
 
# for parsing all the tables present
# on the website
from html_table_parser.parser import HTMLTableParser
 
# for converting the parsed data in a
# pandas dataframe
import pandas as pd
 
 
# Opens a website and read its
# binary contents (HTTP Response Body)
def url_get_contents(url):
 
    # Opens a website and read its
    # binary contents (HTTP Response Body)
 
    #making request to the website
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
 
    #reading contents of the website 
    return f.read()

race_urls=[1064,1065,1066,1086,1067,1068,1070,1092,1071,1072,1073,1074,1075,1076]
race_urls_sprint=[1072,1076]

#races
for i in range(len(race_urls)):
    # defining the html contents of a URL.
    xhtml = url_get_contents('https://www.formula1.com/en/results.html/2021/races/'+str(race_urls[i])+'/bahrain/race-result.html').decode('utf-8')

    # Defining the HTMLTableParser object
    p = HTMLTableParser()

    # feeding the html contents in the
    # HTMLTableParser object
    p.feed(xhtml)
    p=pd.DataFrame(p.tables[0])
    p=np.array(p)

    if race_urls[i] in race_urls_sprint:
        # defining the html contents of a URL.
        xhtml = url_get_contents('https://www.formula1.com/en/results.html/2021/races/'+str(race_urls[i])+'/great-britain/sprint-qualifying-results.html').decode('utf-8')

        # Defining the HTMLTableParser object
        p_2 = HTMLTableParser()

        # feeding the html contents in the
        # HTMLTableParser object
        p_2.feed(xhtml)
        p_2=pd.DataFrame(p_2.tables[0])
        p_2=np.array(p_2)
        p=np.concatenate((p_2,p))

    
    np.save('carrera'+str(i+1),p)

    
 