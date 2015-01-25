#coding=utf-8

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django import forms

import Image
import uuid
import datetime


from courses.models import *

# Create your views here.

#list all courses
def index(req):
	#courses = Course.objects
	#course = courses.first()

	courses = Course.objects

	return render_to_response('index.html', {'courses': courses})

#show the detail of course
#index/1
def show(req, course_id):
	print course_id
#	Course(title='ok', author='supervessel').save()print course_id


	course = Course.objects(id = course_id).first()
	return render_to_response('course.html', {'course': course})

#create a cousre
#/new

class CourseForm(forms.Form):
	title = forms.CharField(label='Title:', max_length=100)
	author = forms.CharField(label='Author:', max_length=100)
	description = forms.CharField(label='Description:', widget=forms.Textarea)
	videoURL = forms.URLField(label='VideoURL:', required = True)

class CodeForm(forms.Form):
	code = forms.CharField(widget=forms.Textarea)


def code(req):
	if req.method == 'POST':

		code = req.POST['code']

		#if form.is_valid():
		#	code = form.cleaned_data['code']
		#	print code
		
		print "c code:", code

	#		return HttpResponseRedirect('/index/')
	#else:

		#form = CodeForm()
	return render_to_response('code.html', {})

def new(req):
	if req.method == 'POST':
		form = CourseForm(req.POST)
		if form.is_valid():
			course = Course()
			
			course.title = form.cleaned_data['title']
			course.author = form.cleaned_data['author']
			course.description = form.cleaned_data['description']
			course.videoURL = form.cleaned_data['videoURL']

			print course
			course.save()
			

			return HttpResponseRedirect('/index/')
	else:
		form = CourseForm()

	return render_to_response('new.html', {'form': form})



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
		return
	else:

		articles = Article.objects(uuid = article_id)
		if len(articles) == 0:
			return HttpResponse("No matched article")
		
		if len(articles) != 1:
			return HttpResponse("too many matched article")
		else:
			for article in articles:
				return render_to_response('publish_article.html', {'article': article})


def newArticle(req):
	if req.method == 'POST':

		print("get parameters")

		title = req.POST['title']
		print "title:", title

		abstract = req.POST['abstract']
		print "abstract:", abstract

		coverImg = req.POST['coverImg']
		print "coverImg:", coverImg

		content = req.POST['content']
		print "content:", content

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
			print "write success:", article.uuid
			url = 'http://127.0.0.1:8000/article/' + article.uuid
			return HttpResponse(url)

		else:
			print "write articole to DB error"
			return HttpResponse(err)

		#if form.is_valid():
		#	code = form.cleaned_data['code']
		#	print code
		#print "title:", title
		#print "abstract:", abstract
		#print "coverImg:", coverImg
		#print "content:", content
		
		#return HttpResponse('ok')
	#		return HttpResponseRedirect('/index/')
	#else:

		#form = CodeForm()
		
	else:
		print "get new_article.html"
		return render_to_response('new_article.html', {})
		



