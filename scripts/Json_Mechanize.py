#!/usr/bin/python

import mechanize
from string import *
import csv

#Accepts - a list of link_ids
#Returns - a tuple where
	#tuple[0] = dictionary of (link_id -> [Library,Author])
	#tuple[1] = array of [library problem ids,author problem ids]

def make_dict(link_ids):
	Dict = {} #id dictionary
	problems = [] #problems array
	br = mechanize.Browser()   # Create a browser
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	BASE_URL = "http://josiah.brown.edu/record="
	counter = 0
	for id in link_ids:
		Dict[id] = ["",""]
		url = BASE_URL + id[0:8]#need to trim id!
		try:
			response = br.open(url)	
			hay = 0
			jcb = 0
			i = 0;
			for l in br.links():
				l = str(l)
				#parse for libraries
				if not hay: 
					hay = find(l,"HAY")!=-1 
				if not jcb:
					jcb = find(l,"JCB")!=-1
				if (hay and jcb): 
					break
				#parse for authors
				if i==14 and find(l,"/browse")!=-1 and find(l,"text=")!=-1:
					start_i = find(l,"text=")+6
					end_i = find(l[start_i:],"',")
					name = l[start_i:start_i+end_i]
					Dict[id][1] = name
				i+=1
			#analyze results of link parsing for libraries
			if (hay and jcb) or (not hay and not jcb):
				problems.append(id)
			elif hay:
				Dict[id][0] = "HAY"
			elif jcb:
				Dict[id][0] = "JCB"
		except:
			print "Error on " + url + " num " + str(counter)
		#Just for tracking progress
		counter+=1
		if not counter % 100:
			print counter
	return (Dict,problems)


'''
make_dict(link_ids)

for i in author_library_dict:
	print i + ": " + author_library_dict[i]

print "PROBLEMS"
for i in problems:
	print i
'''
