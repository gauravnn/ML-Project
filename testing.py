import json
import urllib

def showsome(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read().decode("utf8")
  results = json.loads(search_results)
  print len(results)
  data = results['responseData']
  print len(data)
  print('Total results: %s' % data['cursor']['estimatedResultCount'])
  hits = data['results']
  print len(hits)
  print('Top %d hits:' % len(hits))
  for h in hits: print(' ', h['url'])
  print('For more results, see %s' % data['cursor']['moreResultsUrl'])

showsome('georgia tech uga')
