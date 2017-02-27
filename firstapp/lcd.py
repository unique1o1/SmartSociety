from models import slot
import serial

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

arduinodata.write(b'r')
while True:
    place = slot.objects.all()
    x = []
    y = 0
    for num in place:
        x[y] = num.slotno
        y += 1

    for i in range(0, len(x)):

        a = x[i].encode()

        arduinodata.write(a)
        print(e[i])
    time.sleep(8)
    arduinodata.write(b'r')
