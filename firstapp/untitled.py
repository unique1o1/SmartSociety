from pyfirmata import Arduino, util



class runcommmand():
	def __init__(self):

		board = Arduino('/dev/ttyACM0')
		x=board.get_pin('d:13:i')
		x=x.read()
		return x
def main():
	hey=runcommmand()	

if __name__=="__main__":
	main()