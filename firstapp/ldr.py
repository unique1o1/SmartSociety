from pyfirmata import Arduino, util, Board
import time

def park():
	board=Arduino('/dev/ttyACM2')
	led=board.get_pin('d:13:o')
	i=0
	it = util.Iterator(board)
	it.start()
	yes=1
	no=0
		
	board.analog[0].enable_reporting()
	if i==0:
		time.sleep(1.2)
		i=1
	x=board.analog[0].read()
	print (x)
	if x*1000>40:
		led.write(0)
		return yes
	else:
		led.write(1)
		return no
	board.exit()
def main():
	x=park()
	print(x)
if __name__=="__main__":main()