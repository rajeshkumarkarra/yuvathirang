from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'yuva/index.html')

def single(request):
	return render(request, 'yuva/single.html')

'''def contactform(request):
	print("hello")
	fstname = request.POST['yourname']
	lstname = request.POST['lname']
	myemail = request.POST['myemail']
	mymessage = request.POST['mymessage']
	c= Client(fname=fstname,lname=lstname,email=myemail,message=mymessage)
	c.save()
 
	return render(request,'yuva/index.html')


'''

def emailSubscribe(request):
	print("hello")
	email_s = request.POST['email']
	s= Subscribe(email=email_s)
	s.save()

	return render(request, 'yuva/index.html')