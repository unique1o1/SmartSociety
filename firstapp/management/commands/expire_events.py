from django.core.management import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
from firstapp.models import slot
import pytz
import serial
import time 
import struct
class Command(BaseCommand):

    help = 'Expires event objects which are out-of-date'
    now = timezone.now()
    

    def handle(self, *args, **options):
        arduinodata= serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        time.sleep(.6)
        while True:
            
            
            x=[]
            y=0
            event = slot.objects.all()
            z=0
            for num in event:
            	
                time_over = num.times + timedelta(minutes=3)
                if (time_over < timezone.now()): num.delete()
                else:
                    if z==0:

                        arduinodata.write(b'r')
                        z=1
                    x.append(num.slotno)
                    y =2
            if y!=0:
                spots=len(x)
                arduinodata.write(struct.pack('>B', spots))
                for i in x:
                    if i!=10:
                        strn=str(i)
                    else:
                        strn='a'

                    
                    print(strn)
                    p=strn.encode()
                    print(p)
                    arduinodata.write(p)
                    

                
                time.sleep(10)
            else:
                arduinodata.write(b'c')
                time.sleep(10)



              


                     

                    
                    
                
           	  	
