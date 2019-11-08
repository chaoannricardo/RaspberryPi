import sys

import RPi.GPIO as GPIO

import urllib2

from time import sleep

temper2 = 0


GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers 

RELAIS_1_GPIO = 18

GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode


def getSensorData():

    tempfile = open("/sys/bus/w1/devices/28-051700427aff/w1_slave")

    thetext = tempfile.read()

    tempfile.close()

    tempdata = thetext.split("\n")[1].split(" ")[9]

    temperature = float(tempdata[2:])

    temperature = temperature / 1000

    return (temperature)


# main() function

def main():

    # use sys.argv if needed

    baseURL = 'https://api.thingspeak.com/update?api_key=BTC5HFPKSLIIRCQN'


    while True:

        try:

            temper2 = getSensorData()

            print (temper2)

            if (temper2 > 28) : GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)

            if (temper2 <27) : GPIO.output(RELAIS_1_GPIO, GPIO.LOW) 

            f = urllib2.urlopen(baseURL + "&field1=%s" % (temper2))

            print( f.read())

            f.close()

            sleep(60)

        except:

            print( 'exiting.')

            break


# call main

if __name__ == '__main__':

    main()



