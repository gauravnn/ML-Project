#!/usr/bin/python3
import json
import urllib

def showsome(searchfor):
	query = urllib.urlencode({'q': searchfor})
	url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
	url2 = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&start=4&%s' % query 
	search_response = urllib.urlopen(url)
	search_response2 = urllib.urlopen(url2)
	search_results = search_response.read().decode("utf8")
	search_results2 = search_response2.read().decode("utf8")
	results = json.loads(search_results)
	results2 = json.loads(search_results2)
	data = results['responseData']
	data2 = results2['responseData']
	hits = data['results']
	hits2 = data2['results']
	
	res = list()
	for h in hits: 
		res.append(h['url'])
	for h2 in hits2: 
		res.append(h2['url'])
	
	return res

