import googlemaps
import pandas as pd
import geocoder
import json
import re


data=pd.read_csv('home/ds/notebooks/data/t_links.csv',header=0)
gmaps = googlemaps.Client(key='AIzaSyBEYLI9mwziW4PummB7NOVPt3-FKXqimYQ')


def link_search(data):
	locations=[]
	links=[]
	for linkid,x,y in zip(data['link_id'],data['startY'],data['StartX']):
    	g = gmaps.reverse_geocode((x, y))[0]
    	loc=g['address_components'][3]['short_name']
    	link=linkid
    	locations.append(loc)
    	links.append(link)
    return locations,links
link_search(data)