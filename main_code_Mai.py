#monitoring DHT11 from cloud-ubidots.
import Adafruit_DHT
from ubidots import ApiClient
import RPi.GPIO as GPIO
import time
import serial
smoke=21  #pin 40
pir=20   #pin 38
rel1=19  #relay 1
rel2=26    #relay 2
buz=12    #buzzer

GPIO.setmode(GPIO.BCM)       # GPIO Numbering of Pins
GPIO.setwarnings(False)
GPIO.setup(rel1, GPIO.OUT)   # Set ledPin as output
GPIO.setup(rel2, GPIO.OUT) 
GPIO.setup(pir, GPIO.IN)   # Set switch as input
GPIO.setup(smoke, GPIO.IN)   # Set switch as input
#GPIO.setup(pir, GPIO.IN)
GPIO.setup(buz, GPIO.OUT)

api = ApiClient(token="A1E-bJpcYEuXwhwc0ayFsMxPLT3b02JyYW")

variable1 = api.get_variable("5c6143e7c03f974d81b07d21") #humidity
variable2 = api.get_variable("5c6143d8c03f974d81b07d13")  # temperature
variable3 = api.get_variable("5c61368bc03f973d09c9e55b") #lamp1
variable4 = api.get_variable("5c613695c03f973d09c9e55d") #lamp 2
variable5 = api.get_variable("5c6b9538c03f9740970e4913") #PIR
variable6 = api.get_variable("5c616794c03f977bae4bd82f")  #smoke


while 1:
		humidity, temperature = Adafruit_DHT.read_retry(11, 4)    
		#print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature))
		print "Humidity =", humidity, "%", "Temperature =", temperature, "C"
		#print "Temperature =", temperature, "C" 
		variable1.save_value({'value':humidity})
		variable2.save_value({'value':temperature})
		print"value sent to cloud"
		laf1 = variable3.get_values(1)
		laf2 = variable4.get_values(1)
		print laf1
		print laf2
        	a = laf1[0]['value']
		b = laf2[0]['value']
        	#print a
		#print b
 		if a == 0.0 and b==0.0:
                	GPIO.output(rel1,True)
                	print "LIGHT 1 Off"
			GPIO.output(rel2,True)
                	print "LIGHT 2 Off"

	        elif a == 0.0 and b==1.0:
                	GPIO.output(rel2,True)
                	print "LIGHT 1 Off"
			GPIO.output(rel1,False)
                	print "LIGHT 2 On"

	        elif a == 1.0 and b==0.0:
        	        GPIO.output(rel2,False)
                	print "LIGHT 1 On"
			GPIO.output(rel1,True)
                	print "LIGHT 2 Off"
		else:
			GPIO.output(rel1,False)
                	print "LIGHT 1 On"
			GPIO.output(rel2,False)
                	print "LIGHT 2 On"
		if GPIO.input(smoke)==0:
                        sm=1
                        print 'smoke detected'
                        variable4.save_value({'value':sm})
                        #GPIO.output(ledPin, GPIO.HIGH)   # LED On
                        #time.sleep(1)                  # wait 1 sec
                elif GPIO.input(smoke)==1:
                        m=0
                        print 'smoke  not detected '
                        variable4.save_value({'value':m})
                        #GPIO.output(ledPin, GPIO.LOW)   # LED Off
                        #time.sleep(1)                 # wait 1 sec
		if GPIO.input(pir)==1:
			obj_found=1
			print 'PIR detected'
			variable5.save_value({'value':obj_found})
                	#GPIO.output(ledPin, GPIO.HIGH)   # LED On
                	time.sleep(1)                  # wait 1 sec
        	elif GPIO.input(pir)==0:
			obj_not_found=0
                	print 'PIR not detected '
			variable5.save_value({'value':obj_not_found})
                	#GPIO.output(ledPin, GPIO.LOW)   # LED Off
                	#time.sleep(1)                 # wait 1 sec

'''	if GPIO.input(ir)==1:
			d=1
			print 'IR detected'
			variable3.save_value({'value':d})
                	#GPIO.output(ledPin, GPIO.HIGH)   # LED On
                	#time.sleep(1)                  # wait 1 sec
                elif GPIO.input(ir)==0:
			nd=0
                	print 'IR not detected '
			variable3.save_value({'value':nd})
                	#GPIO.output(ledPin, GPIO.LOW)   # LED Off
                	#time.sleep(1)                 # wait 1 sec
		if GPIO.input(smoke)==0:
                        sm=1
                        print 'smoke detected'
                        variable4.save_value({'value':sm})
                        #GPIO.output(ledPin, GPIO.HIGH)   # LED On
                        #time.sleep(1)                  # wait 1 sec
                elif GPIO.input(smoke)==1:
                        m=0
                        print 'smoke  not detected '
                        variable4.save_value({'value':m})
                        #GPIO.output(ledPin, GPIO.LOW)   # LED Off
                        #time.sleep(1)                 # wait 1 sec
		if GPIO.input(pir)==1:
			obj_found=1
			print 'PIR detected'
			variable5.save_value({'value':obj_found})
                	#GPIO.output(ledPin, GPIO.HIGH)   # LED On
                	time.sleep(1)                  # wait 1 sec
        	elif GPIO.input(pir)==0:
			obj_not_found=0
                	print 'PIR not detected '
			variable5.save_value({'value':obj_not_found})
                	#GPIO.output(ledPin, GPIO.LOW)   # LED Off
                	#time.sleep(1)                 # wait 1 sec'''
