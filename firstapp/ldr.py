from pyfirmata import Arduino, util, Board
import time

def park():
	board=Arduino('/dev/ttyACM0')
	
	i=0

	cars=0
	it = util.Iterator(board)
	it.start()
	
	# while cars<10:
	# 	board.analog[cars].enable_reporting()board.analog[cars].enable_reporting()
	# 	cars=cars+1
	board.analog[0].enable_reporting()
	board.analog[1].enable_reporting()
	board.analog[2].enable_reporting()
	# board.analog[3].enable_reporting()
	# board.analog[4].enable_reporting()	
	# board.analog[5].enable_reporting()

	if i==0:
		time.sleep(1.2)
		i=1
	cars=0
	output=[2,2,2,2,2,2,2,2,2,2]	
	while cars<3:	
		x=board.analog[cars].read()
		print (x*1000)
		if x*1000>200:
			# led.write(0)
			output[cars]=1
			print(output)

		else:
			# led.write(1)
			output[cars]=0
			
		cars=cars+1
	# return output
	board.exit()
def main():
	park()
	
if __name__=="__main__":main()
