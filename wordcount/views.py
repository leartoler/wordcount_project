from django.http import HttpResponse
from django.shortcuts import render
import operator

def home (request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			# incrementa
			worddictionary [word] += 1
		else:
			#lo suma al diccionario
			worddictionary [word] = 1

		sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

	#De aqupi en adelante es ara agregar cualquier cosa nueva que se pueda cocurrir, el cielo es el límite. 
	

