import os
import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import requests
import subprocess

pir_SENSOR_PIN = 7 #GPIO input pin 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_SENSOR_PIN, GPIO.IN)
count = 0


MQTT_SERVER = "192.168.0.106"
MQTT_PATH = "sense_presence"

try:
    while True:
        if (GPIO.input(pir_SENSOR_PIN)): #detection
            print("Movement Detected")
            data = 1
            #print(data)
            payload = str(data)
            #print(payload)
            #publishing the data to the mqtt broker
            publish.single(MQTT_PATH, payload, hostname=MQTT_SERVER)
            time.sleep(.5)
            #data.clear()
        
            
except KeyboardInterrupt:
        print("Beende...")
        GPIO.cleanup()
