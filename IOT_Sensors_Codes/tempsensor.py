import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import requests
import subprocess
import os
import RPi.GPIO as GPIO
import adafruit_dht
from board import *

SENSOR_PIN =D17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
dht_device = adafruit_dht.DHT22(SENSOR_PIN,use_pulseio= False) #temp
MQTT_SERVER = "192.168.0.106"
MQTT_PATH = "sense_temp"

#print("Hello")


def readSensorData():
    global tempSensor
    tempSensor = data
while True:
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        #print(humidity)
        #time.sleep(15)
        data = temperature    
        print("Temperature (Celsius) is:",temperature)
        readSensorData()
        payload = "2" + "," + str(data)
        #print(payload)
        publish.single(MQTT_PATH, payload, hostname=MQTT_SERVER)
        time.sleep(10)
    except RuntimeError:
        print("initialising")
        continue
    
