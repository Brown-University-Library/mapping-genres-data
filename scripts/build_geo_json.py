#!/usr/bin/python

#this script builds a GeoJson file, using the book json and the bookless geo-json as template files
#the script is dependant on Json_Mechanize.py, which uses the mechanize module
import  json
from Json_Mechanize import make_dict



with open('2014-08-01GeoJsonLocations.json') as infile:
	with open('2014-05-20HayJCBBooks.json') as book_file:
		with open('2014-08-18GeoJsonLocations.json','w') as out_locations:
			with open('2014-08-18HayJCBBooks.json','w') as out_books:
				jsonData = json.load(infile)
				bookData = json.load(book_file)
				books = [] #new book array
				ids = []
				for book in (bookData['rows']):
					ids.append(book['bib'])
					books.append(book)
				tup = make_dict(ids)
				Dict = tup[0]
				problems =  tup[1]
				for location in jsonData['rows']:
					for book in books:
						if book["GeoPlace"] == location['properties']['name']:
							book["Library"] = Dict[book['bib']][0]
							book["Author"] = Dict[book['bib']][1]
							#book["Language"] = Dict[book['bib']][2]
							location['properties']['books'].append(book);
		  		json.dump(jsonData,out_locations)
		  		json.dump(books,out_books)




