from pyfirmata import ArduinoMega, util
import time

def park():
    board = ArduinoMega('/dev/ttyACM0')
    i = 0

    cars = 0
    it = util.Iterator(board)
    it.start()

    while cars < 10:
        board.analog[cars].enable_reporting()
        cars = cars + 1

    l = 0
    if i == 0:
        time.sleep(1.2)
        i = 1

    output = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    cars = 0
    while cars < 10:
        x = board.analog[cars].read()

        if 500 < x * 1000:
        # if 20>x*1000:
            output[cars] = 0
                # led.write(0)

        cars = cars + 1
    for j in range(0, 10):
        l = l + output[j]

    output.append(l)

        # if l==10:
        # 	board.digital[13].write(1)
   
    return output
    board.exit()
     

def main():

    park()

if __name__ == "__main__":
    main()
