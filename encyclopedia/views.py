from django.core.files.storage import default_storage
from django.http import request

from django.shortcuts import render,redirect

from . import util
from random import randint
from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
   
  
    
def entry(request,title):
    content = util.get_entry(title.strip())
    if content == None:
        content =" ## page not found"
    content = markdown(content)
    return render(request,"encyclopedia/entry.html",{
        'content': content, 'title': title})




def new_page(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("body")
        if title=="" or content=="":
            return render(request,"encyclopedia/new_page.html",{"message":"can't save an empty entry","title":title,"content":content})
        if title in util.list_entries():
            return render(request,"encyclopedia/new_page.html",{"message":"this already exists, try another one or just edit ","title":title,"content":content})

        util.save_entry(title,content)
        return redirect("post",title=title)
    return render(request,"encyclopedia/new_page.html")




def search(request):
    q = request.GET.get('q').strip()
    if q in util.list_entries():
        return redirect("post",title=q)
    return render(request,"encyclopedia/search.html", {
        "entries":util.search(q), "q":q
        })


def random(request):
    entry=util.list_entries()
    title = entry[randint(0,len(entry)-1)]
    return redirect("post",title=title)
    
    

def edit(request,title):

    content = util.get_entry(title)

    if content == "None":

        return render(request,"encyclopedia/edit.html",{"error":"page not found "})

    if request.method=="POST":

        content = request.POST.get("content")

        if content == "":
            return render(request, "encyclopedia/edit.html", {"message": "Can't save with empty field.", "title": title, "content":content})

        util.save_entry(title, content)

        return redirect("post",title=title)
    return render(request,"encyclopedia/edit.html",{
        'content':content , 'title':title   
        
         })
        
"""              

def edit(request, title):
    content = util.get_entry(title.strip())
    if content == None:
        return render(request, "encyclopedia/edit.html", {'error': "404 Not Found"})

    if request.method == "POST":
        content = request.POST.get("content").strip()
        if content == "":
            return render(request, "encyclopedia/edit.html", {"message": "Can't save with empty field.", "title": title, "content": content})
        util.save_entry(title, content)
        return redirect("entry", title=title)
    return render(request, "encyclopedia/edit.html", {'content': content, 'title': title})








"""