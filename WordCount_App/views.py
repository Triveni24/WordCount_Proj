from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def home(request):
    return render(request,'home.html')

def count(request):
    fulltext1=request.GET['fulltext1']
    wordlist=fulltext1.split()

    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1

    return render(request,'count.html',{'fulltext1':fulltext1,'count':len(wordlist), 'worddictionary':worddictionary.items()})


def about(request):
    return render(request,'about.html')
