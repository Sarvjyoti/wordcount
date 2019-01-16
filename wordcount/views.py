from django.http import HttpResponse
from django.shortcuts import render
#for operator
import operator



#if you want to access html page then can't pass httpresponse directly
# def homepage(request):
# 	return HttpResponse('<h1>Congretulations!<br> You completed first Django Program') #we cant return directly

#for html page
# def homepage(request):
# 	return render(request,'home.html')



#for dictionary in python
def homepage(request):
 	return render(request,'home.html')



def count(request):
	data = request.GET['fulltextarea']
	word_list=data.split()
	list_lenght = len(word_list)

	#forcounting words occurance
	worddictionary = {}
	for word in word_list:
		if word in worddictionary:
			#increase value by 1
			worddictionary[word] +=1
		else:
			#add to the dictionary and set value to 1
			worddictionary[word] = 1


	sorted_list = sorted(worddictionary.items(), key = operator.itemgetter(1)) # here we can pass 1 or 0
	return render(request, 'count.html',{'fulltext':data, 'words': list_lenght, 'worddictionary':sorted_list})