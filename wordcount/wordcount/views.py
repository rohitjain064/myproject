from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,"index.html",{"name":"hi there this is rohit"})



def contact(request):
    return render(request,'contact.html')

def count(request):
    data=request.GET['fulltextarea']
    word_list=data.split()
    word_len=len(word_list)
    word_dic={}
    for word in word_list:
        if word in word_dic:
            word_dic[word]+=1
        else:
            word_dic[word]=1
    sorted_list=sorted(word_dic.items(),key=operator.itemgetter(1),reverse=True)







    return render(request,'count.html',{'fulltextarea':data,'words':word_len,'word_dict':sorted_list})