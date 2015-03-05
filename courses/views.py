#coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django import forms

import Image
import uuid
import datetime

import urllib,httplib
import json

from courses.models import *
from SuperClass.settings import *

# Create your views here.

def articles(req):

	if req.method == 'POST':
		return
	else:
		articles = Article.objects.order_by("-createdTime")
		#articles = a.reverse()
		if len(articles) == 0:
			return HttpResponse("No matched article")
		else:
			return render_to_response('articles.html', {'articles': articles})



def article(req, article_id):

	if req.method == 'POST':
		return;
	else:

		articles = Article.objects(uuid = article_id)
		if len(articles) == 0:
			return HttpResponse("No matched article")
		
		if len(articles) != 1:
			return HttpResponse("too many matched article")
		else:
			return render_to_response('article.html', {'article': articles[0]})


def index(req):
	if req.method == 'POST':
		return
	else:
		articles = Article.objects.order_by("-createdTime")
		#articles = a.reverse()
		if len(articles) == 0:
			return HttpResponse("No matched article")
		else:
			return render_to_response('index_articles.html', {'articles': articles})


def new(req):
	if req.method == 'POST':
		title = req.POST['title']
		abstract = req.POST['abstract']
		coverImg = req.POST['coverImg']
		content = req.POST['content']


		#check upload image size
		if len(coverImg) > 300 * 1024:
			err = "cover image is bigger than 100KB"
			return HttpResponse(err)

		if len(content) > 500 * 1024:
			err = "content is bigger than 300KB"
			return HttpResponse(err)

		article = Article()
		article.uuid = uuid.uuid1().hex
		article.title = title
		article.abstract = abstract
		article.coverImg = coverImg
		article.content = content
		article.createdTime = datetime.datetime.now

		if article.save():
			url = '/admin/article/' + article.uuid
			return HttpResponse(url)

		else:
			print "write articole to DB error"
			return HttpResponse(err)
	else:
		return render_to_response('new_article.html', {})


def review(req, article_id):
	if req.method == 'POST':
		return		
	else:
		articles = Article.objects(uuid = article_id)
		if len(articles) == 0:
			return HttpResponse("No matched article")
		
		if len(articles) != 1:
			return HttpResponse("too many matched article")
		else:
			return render_to_response('review_article.html', {'article': articles[0]})


def delete(req,article_id):
	if req.method == 'POST':
		return		
	else:
		article = Article.objects(uuid = article_id)[0]
		
		if article:
			article.delete()
		
		return HttpResponseRedirect('/admin/article/index')

#post article_id to external server
def publish(req, article_id):
	if req.method == 'POST':
		return
	else:
		articles = Article.objects(uuid = article_id)
		if len(articles) == 0:
			return HttpResponse("No matched article")

		if len(articles) != 1:
			return HttpResponse("too many matched article")

		else:

			#params = urllib.urlencode(
			#	{ 'uuid': articles[0].uuid.hex,
			#	  'title': articles[0].title,
			#	  'abstract': articles[0].abstract,
			#	  'coverImg': articles[0].coverImg,
			#	  'content': articles[0].content,
			#	  'createdTime': articles[0].createdTime
			#	 }
			#)
			params = { 'uuid': articles[0].uuid.hex,
				  'title': articles[0].title,
				  'abstract': articles[0].abstract,
				  'coverImg': articles[0].coverImg,
				  'content': articles[0].content,
				  'createdTime': articles[0].createdTime.isoformat()
				 }

			headers = {"Content-Type":"application/json"}

			httpClient = httplib.HTTPConnection(PUBLISH_HOST)
			httpClient.request("POST", PUBLISH_URL, json.dumps(params), headers)

			response = httpClient.getresponse()

			#print response.read()
			
			return HttpResponse(response.read())

def accept(req):
	if req.method == 'POST':
		
		return HttpResponse(
			req.POST['uuid'] + 
			req.POST['title'] +
			req.POST['abstract'] +
			req.POST['coverImg'] +
			req.POST['content'] +
			req.POST['createdTime']
		)