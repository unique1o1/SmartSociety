from models import slot
import serial

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

arduinodata.write(b'r')
while True:
    place = slot.objects.all()
    x = [num.slotno for num in place]

    for i in range(0, len(x)):

        a = x[i].encode()

        arduinodata.write(a)
        print(e[i])
    time.sleep(8)
    arduinodata.write(b'r')
