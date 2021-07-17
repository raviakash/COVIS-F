import RPi.GPIO as GPIO
import os
import time
import subprocess
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

MQTT_SERVER = "192.168.0.106"
MQTT_PATH = "sense_count"

    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ir1=12
ir2=13

GPIO.setup(ir1,GPIO.IN)#GPIO 12 -> IR sensor 1 as input
GPIO.setup(ir2,GPIO.IN)#GPIO 13 -> IR sensor 2 as input

count1 = 0
count2 = 0   
  
while True:
    
    if(GPIO.input(ir1)==False): #detection
        #print("hi")
        count1 = count1 + 1#count of people from entry
        #print(count1)
        payload2= "1"+","+ str(count1)
        
        publish.single(MQTT_PATH, payload2, hostname=MQTT_SERVER)
        time.sleep(1)
    
    if(GPIO.input(ir2)==False): #detection
        count2 = count2 + 1#count of people from exit
        #print("bye")
        #print(count2)
        time.sleep(1)
    count = count1 - count2 #existing people inside
    print("Total people inside : ", count)
    payload = "2"+","+ str(count)
    #payload2= str(count1)
    #publish the data to the MQTT broker
    publish.single(MQTT_PATH, payload, hostname=MQTT_SERVER)
    #publish.single(MQTT_PATH, payload2, hostname=MQTT_SERVER)
    time.sleep(.3)
    #payload.clear()
