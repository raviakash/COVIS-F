import RPi.GPIO as GPIO
import Adafruit_DHT
import os
import time
import subprocess
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

#sensor used TCS3200
MQTT_SERVER = "192.168.0.106"
MQTT_PATH = "sense_rgb"
temp=1
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
s2 = 23 #GPIO 23
s3 = 24 #GPIO 24 
signal = 25 #
switch=15
NUM_CYCLES = 10
GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s2,GPIO.OUT)
GPIO.setup(s3,GPIO.OUT)
GPIO.setup(switch,GPIO.IN)
countA = 10
countB = 10
payload5 = 10
payload4 = 10
data=""
payload=""
while True:
        #initialising red
        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.LOW)
        time.sleep(0.1)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start      #seconds to run for loop
        red  = NUM_CYCLES / duration   #in Hz
        #print("red value - ",red)

        #initialising blue
        GPIO.output(s2,GPIO.LOW)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.1)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        blue = NUM_CYCLES / duration
        #print("blue value - ",blue)


        #initialising green
        GPIO.output(s2,GPIO.HIGH)
        GPIO.output(s3,GPIO.HIGH)
        time.sleep(0.1)
        start = time.time()
        for impulse_count in range(NUM_CYCLES):
          GPIO.wait_for_edge(signal, GPIO.FALLING)
        duration = time.time() - start
        green = NUM_CYCLES / duration
        #print("green value - ",green)

        #detection of red color
        if GPIO.input(switch) == GPIO.HIGH:
            entry =0
            if green<red and blue<red and red>300:
                print("Vaccine - Moderna Access Granted")
                temp=1
                data = "red"
                #deduct vaccine A
                countA = countA - 2
                entry=1
        
            #detection of blue color
            elif blue>red and  blue>green and green>0:
                print("Vaccine - Pfizer Access Granted")
                temp=1
                data = "green" #note : just sending data as green for our ease of work
          
                countB = countB - 2
        
                entry=1
            #detection of green color
            elif green>red and green>blue and green>0:
                print("Vaccine - Restocking Access Granted")
                temp=1
                data = "blue"

                countA=10
                countB=10
                entry=1
          
            elif red<300 and green<300 and blue<300:
                print("place the card.....")
      #rgb actuator
                temp=0
            if(entry==1):
                payload = str(data)
                payload4=str(countA)
                payload5=str(countB)
                #publishing to mqtt broker
                publish.single(MQTT_PATH, payload, hostname=MQTT_SERVER)
                publish.single(MQTT_PATH, payload4, hostname=MQTT_SERVER)
                publish.single(MQTT_PATH, payload5, hostname=MQTT_SERVER)
                entry=0        
        
        
        
       
    #data2.clear()
    #data3.clear()
