from django.shortcuts import render
from django.http import Http404
import json
from firstapp.models import item
from firstapp.ldr import park
# Create your views here.

def home(request):
	# x=runcommmand()
	# items=item(title='sajesh', amount=12)
	# items.save()
	# items=item(title='sat', amount=12)
	# items.save()
	# items.title='sajesh1'
	# items.save()

	# arduinodata= serial.Serial('/dev/ttyACM0', 9600, timeout=1)
   
	# data=arduinodata.readline().decode('ascii')
 
	# items=item.objects.all()
	
	return render(request,'firstapp/home.html') 

def homestatus(request):
	return render(request,'firstapp/homestatus.html')

def environment(request):
	return render(request,'firstapp/environment.html')
def parking(request):
	# x=[1,2,3,4,5,6]
	x= park()
	return render(request,'firstapp/parking.html',{'x':x})