from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import Blog,Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login,logout
from blog.forms import signinForm,registerForm,create_blogForm
import time

def home(request):
	blogs=Blog.objects.all()
	return render(request,'home.html',{'blogs':blogs})

def signin(request):
	error=False
	request.session['login_from']=request.META.get('HTTP_REFERER','/')
	if request.method=='POST':
		form=signinForm(request.POST)
		if form.is_valid():
			user=form.cleaned_data['name']
			password=form.cleaned_data['password']
			user=auth.authenticate(username=user,password=password)
			if user and user.is_active:
				auth.login(request,user)
				return HttpResponseRedirect('/')
			else:
				error='账号或密码错误'
	else:
		form=signinForm()
	return render(request,'signin.html',{'form':form ,'error':error})
def signout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def register(request):
	error=False
	if request.method=='POST':
		form=registerForm(request.POST)
		if form.is_valid():
			user=form.cleaned_data['name']
			password1=form.cleaned_data['password1']
			password2=form.cleaned_data['password2']
			email=form.cleaned_data['email']
			if password1==password2:
				password=password2
				user = User.objects.create_user(username=user,email=email,password=password)
				return HttpResponseRedirect('/signin')
			else:
				error=True
	else:
		form=registerForm()
	return render(request,'register.html',{'form':form,'error':error})


def blogs(request):
	if request.user.is_staff:
		blogs=Blog.objects.all()
		#summary='Lorem ipsum dolor sit amet,consectetur adipisicing elit,sed do eiusmod tempor incididunt ut labore et dolore megna aliqua'
		#blogs=[
		#	Blog(name='Test Blog',summary=summary),
		#	Blog(name='Something New',summary=summary),
		#	Blog(name='Learn Swift',summary=summary)]
		return render(request,'blogs.html',{'blogs':blogs})
	else:
		return HttpResponseRedirect('/')


def blog(request,name):
	name=name
	error=False
	if request.method=='POST':
		if  request.user.is_anonymous():
			error=True
			#return render(request,'blog.html',{'blog':blog,'comments':comments,'error':error})
		else:
			content=request.POST['comment']
			blog_name=name
			user_name=request.user.username
			c=Comment(blog_name=name,user_name=user_name,content=content)
			c.save()
	try:
		blog=Blog.objects.get(name=name)
		comments=Comment.objects.filter(blog_name=name)
	except:
		blog=False
		comments=False
	return render(request,'blog.html',{'blog':blog,'comments':comments,'error':error})

def delete(request,name):
	name=name
	if user.is_staff:
		blog=Blog.objects.filter(name=name).delete()
		return HttpResponseRedirect('/blogs')
		

def change(request,name):
	name=name
	error=[]
	if request.method=='POST':
		title=request.POST['title']
		summary=request.POST['summary']
		content=request.POST['content']
		if not title.strip():
			error.append('标题不能为空')
		elif not summary.strip():
			error.append('概要不能为空')
		elif not content.strip():
			error.append('请填写日志内容')
		else:
			blog=Blog.objects.filter(name=name).update(name=title,summary=summary,content=content)
			return HttpResponseRedirect('/blogs')
	blog=Blog.objects.get(name=name)
	return render(request,'create_blog.html',{'blog':blog,'error':error})

def create_blog(request):
	error=[]
	if request.method=='POST':
		title=request.POST['title']
		summary=request.POST['summary']
		content=request.POST['content']
		user_name=request.user.username
		if not title.strip():
			error.append('标题不能为空')
		elif not summary.strip():
			error.append('概要不能为空')
		elif not content.strip():
			error.append('请填写日志内容')
		else:
			blog=Blog(user_name=user_name,name=title,summary=summary,content=content)
			blog.save()
			return HttpResponseRedirect('/blogs')
	return render(request,'create_blog.html',{'error':error})
	


def comments(request):
	if request.user.is_staff:
		comments=Comment.objects.all()
		return render(request,'comments.html',{'comments':comments})
	else:
		return HttpResponseRedirect('/')


def yonghu_list(request):
	if request.user.is_staff:
		user_list=User.objects.all()
		return render(request,'user_list.html',{'user_list':user_list})
	else:
		return HttpResponseRedirect('/')
def comment_delete(request):
	pass

def yonghu_delete(request):
	pass

