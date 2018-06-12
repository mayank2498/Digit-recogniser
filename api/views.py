from django.shortcuts import render

def index(request):
	print("get req")
	return render(request,'api/main.html')