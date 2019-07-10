from django.http import HttpResponse
from django.shortcuts import render

# method view index
def index(request):

	judul = "<h1> ini adalah Home </h1>"
	subjudul = "<h2> selamat datang di website ini </h2>"

	output = judul + subjudul;
	return HttpResponse(output)

def about(request):
	content = render(request,'about.html')
	
	return content