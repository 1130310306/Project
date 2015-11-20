#coding=utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import Book,Author
import sqlite3

def Home(req):
    return render_to_response('Home.html')
def Books_show(req):
    book_list = Book.objects.all()
    return render_to_response('Book.html',{'book_list':book_list},context_instance=RequestContext(req))
def Author_find(req):
    fdbooks=[]
    if req.GET:
        fdauthor=Author.objects.filter(Name=req.GET["authorname"])
        if len(fdauthor) != 0:
           fdid=fdauthor[0].AuthorID
           fdbooks=Book.objects.filter(AuthorID=fdid)
           return render_to_response('Author.html',{'fdauthor':fdauthor[0].Name,'fdbooks':fdbooks},context_instance=RequestContext(req))
        else:
           return render_to_response('Author.html',{'fdauthor':req.GET["authorname"],'fdbooks':fdbooks},context_instance=RequestContext(req))
    return render_to_response('Author.html',{'fdauthor':"Author",'fdbooks':fdbooks},context_instance=RequestContext(req))
def delete(req):
    oneid=req.GET["id"]
    debook=Book.objects.get(id=oneid)
    Book.objects.filter(id=oneid).delete()
    return render_to_response('delete.html',{'debook':debook},context_instance=RequestContext(req))
def details(req):
    oneid=req.GET["id"]
    dtbook=Book.objects.get(id=oneid)
    dtauthor=Author.objects.get(AuthorID=dtbook.AuthorID)
    return render_to_response('details.html',{'dtbook':dtbook,'dtauthor':dtauthor},context_instance=RequestContext(req))
def update(req):
    oneid=req.GET["id"]
    upbook=Book.objects.filter(id=oneid)
    upauthor=Author.objects.filter(AuthorID=upbook[0].AuthorID)
    if req.POST:
        Author.objects.filter(AuthorID=upbook[0].AuthorID).update(Name=req.POST["Author"])
        Book.objects.filter(id=oneid).update(Publisher=req.POST["Publisher"])
        Book.objects.filter(id=oneid).update(Price=req.POST["Price"])
        return render_to_response('update.html',{'upbook':Book.objects.filter(id=oneid)[0],'text':"Submit Successfully!",'upauthor':Author.objects.filter(AuthorID=upbook[0].AuthorID)[0]},context_instance=RequestContext(req))
    return render_to_response('update.html',{'upbook':upbook[0],'text':"",'upauthor':upauthor[0]},context_instance=RequestContext(req))
def addbook(req):
    if req.POST:
        Book.objects.create(ISBN=req.POST["ISBN"],Title=req.POST["Title"],Publisher=req.POST["Publisher"],PublishDate=req.POST["PublishDate"],Price=req.POST["Price"],AuthorID=0)
        author=Author.objects.filter(Name=req.POST["Author"])
        if len(author) != 0:
            Author.objects.filter(ISBN=req.POST["ISBN"]).update(AuthorID=author.AuthorID)
            return render_to_response('addbook.html',{'text':"Add Book Successfully ! The author of the book is already exist, There is no need to add an author for this book."},context_instance=RequestContext(req))
        else:
            return render_to_response('addbook.html',{'text':"Add Book Successfully ! The author of the book doesn't exist, You need to click the botton bollow to add an author for this book."},context_instance=RequestContext(req))
    return render_to_response('addbook.html',{'text':""},context_instance=RequestContext(req))
def addauthor(req):
    if req.POST:
        Author.objects.create(AuthorID=req.POST["AuthorID"],Age=req.POST["Age"],Name=req.POST["Name"],Country=req.POST["Country"])
        return render_to_response('addauthor.html',{'text':"Add Author Successfully !"},context_instance=RequestContext(req))
    return render_to_response('addauthor.html',{'text':""},context_instance=RequestContext(req))