from django.shortcuts import render
from django.http import Http404
import json
from firstapp.models import item,slot
from firstapp.ldr import park
from .forms import support
from django.http import HttpResponseRedirect
from datetime import datetime

# Create your views here.
global_var=[]

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
	global global_var
	global_var = park() 
	place=slot.objects.all()
	for num in place:
		global_var[num.slotno-1]=2
		flag=global_var[10]
		global_var[10]=flag-1

	return render(request,'firstapp/parking.html',{'x':global_var,'space':global_var[10]})
def support(request):
	return render(request, 'firstapp/support.html')
def getslot(request):
	
	val=int(request.POST['hiddenfield'])

	slotdata=slot(slotno=val, slotid=request.POST['code'], times=datetime.now())

	slotdata.save()
	
	global_var[val-1]=2
	flag=global_var[10]
	global_var[10]=flag-1

	return render(request, 'firstapp/parking.html',{'x':global_var,'space':global_var[10]})
def getmessage(request):
	info = item(name=request.POST['your_name'],message=request.POST['your_message'],number=request.POST['your_number'],email=request.POST['your_email'])
	info.save()
	return render(request,'firstapp/home.html')
	# if request.method == 'POST':
		# # create a form instance and populate it with data from the request:
		# form = support(request.POST)
		# # check whether it's valid: 

		# if form.is_valid():
		# 	info=item(name=form.cleaned_data['your_name'],message=form.cleaned_data['your_message'],number=form.cleaned_data['your_number'],email=form.cleaned_data['your_email'])
		   	
		# 	info.save()
			
		# else:
		# 	form = support()
		# return render(request, 'firstapp/name.html', {'form': form})
        		
  #        # process the data in form.cleaned_data as required
  #           # ...
  #           # redirect to a new URL:
            

  #   # if a GET (or any other method) we'll create a blank form
    
        
    
            
        
        
        
        
           

    