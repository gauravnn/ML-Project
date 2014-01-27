import nltk
from nltk.corpus import names
import random
import csv
import itertools
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
from nltk.classify import MaxentClassifier
from nltk.classify import NaiveBayesClassifier

def gender_features(word):
	return {'last_letter': word[-1]}
	
def convert1(arr):
	s= '';
	for row in arr:
		s = s +' '+ row
	s = s[1:]
	return s
	
def feature_extractor(row):
	words = nltk.tokenize.word_tokenize(row)
	#fdist = nltk.FreqDist(words)
	#fdist1 = words
	fdist1 = nltk.bigrams(words)
	
	res = ([{'bigram' : convert1(temp)} for temp in fdist1])
	return res

	

cr = csv.reader(open("Data/Dataset1.csv","rb"))
#for rows in cr:
#	print rows,'\n'


temp = [(row[1], row[0]) for row in cr]

data_set_total = []
for (t1,t2) in temp:
	data_set_total = data_set_total + [(a1,t2) for a1 in feature_extractor(t1)]


#data_set_total = [(tp1 for tp1 in feature_extractor(row[1]), row[0]) for row in cr]
train_set, test_set = data_set_total[:800], data_set_total[800:]
classifier = NaiveBayesClassifier.train(train_set)
#feature_extractor(row[1])

print classifier.classify(feature_extractor('How are')),' How are you'

"""
names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
random.shuffle(names)

featuresets = [(gender_features(n), g) for (n,g) in names]
"""

print data_set_total[:20],'\n'

#print featuresets[:20]
#train_set, test_set = featuresets[500:], featuresets[:500]
#classifier = nltk.NaiveBayesClassifier.train(train_set)

"""
print classifier.classify(gender_features('Neo')),' Neo'
print classifier.classify(gender_features('Tirodkar')),' Tirodkar'
print classifier.classify(gender_features('Siddharth')),' Siddharth'
print classifier.classify(gender_features('Thiagarajan')),' Thiagarajan'
print classifier.classify(gender_features('Sagar')),' Sagar'
print classifier.classify(gender_features('Neeraja')),' Neeraja'
print classifier.classify(gender_features('Varsha')),' Varsha'
print classifier.classify(gender_features('Niharika')),' Niharika'
print classifier.classify(gender_features('Rashmi')),' Rashmi'
print classifier.classify(gender_features('Gaurav')),' Gaurav'
print classifier.classify(gender_features('Jayashree')),' Jayashree'
print gender_features('Hello')
"""

