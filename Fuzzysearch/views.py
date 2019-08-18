from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

import json

# Create your views here.
def fuzzy_search(request,word):
    print(word)

    if(request.method=="GET"):
        with open('word_search.tsv') as csvfile:
            data = pd.read_csv(csvfile, delimiter='\t', header=None, index_col=False)#reading the data from file
            data["Indexes"] = data[0].str.find(word)#searching for the words containing the subword, If present returns the index
            data = data[data['Indexes'] > -1]#removing words that donot contain subword
            data = data.sort_values('Indexes')#sorting data based on index
            datb = data.head(25)#fetching top25 results
            datc = datb.sort_values(1, ascending=False)#sorting values based on frequency of the word
            array = []
            for index, row in datc.iterrows():#created a 2d array and inserting word and its frequency
                lists = []
                lists.append(row[0])
                lists.append(row[1])
                array.append(lists)
            array = sorted(array, key=lambda x: (x[1], -len(x[0])), reverse=True)#if word is of same frequency then sort by word length
            j_array = []
            for i in array:
                j_array.append(i[0])
            print(j_array)#contains all the words in order
    return HttpResponse(json.dumps(j_array))


#WITH_UI
def template_view(request):
    j_array = []
    login_data = request.GET.dict()
    username = login_data.get("username")
    if(username!=None):
        if (request.method == "GET"):
            with open('word_search.tsv') as csvfile:
                data = pd.read_csv(csvfile, delimiter='\t', header=None, index_col=False)
                data["Indexes"] = data[0].str.find(username)
                data = data[data['Indexes'] > -1]
                data = data.sort_values('Indexes')
                datb = data.head(25)
                datc = datb.sort_values(1, ascending=False)
                array = []
                for index, row in datc.iterrows():
                    lists = []
                    lists.append(row[0])
                    lists.append(row[1])
                    array.append(lists)
                array = sorted(array, key=lambda x: (x[1], -len(x[0])), reverse=True)
                for i in array:
                    j_array.append(i[0])
        return HttpResponse(json.dumps(j_array))
    return render(request,"word_search/form.html")

