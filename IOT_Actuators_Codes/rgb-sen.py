import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

servoPIN = 26  #servo
servoPIN2 = 18  #servo
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # to disable GPIO warnings at run time
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN2,GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p2 = GPIO.PWM(servoPIN2, 50) # GPIO 18 for PWM with 50Hz
p.start(2.5)
p2.start(0)
print("\n")


MQTT_SERVER = "192.168.0.106"
MQTT_PATH = "room_motor"

#connect to broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    client.subscribe(MQTT_PATH)

#recieve message
def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))


    payloadData = msg.payload.decode('utf-8')
    payloadDataValues = payloadData

    #    print(payloadDataValues)
    #rotate motor of vaccine A
    if (int(payloadData) == 2 ):
        print("hi")
        p.ChangeDutyCycle(2.5)
        time.sleep(.5)
        p.ChangeDutyCycle(5)
        time.sleep(.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(5)
        p.ChangeDutyCycle(5)
        time.sleep(.5)
        p.ChangeDutyCycle(2.5)
        time.sleep(.5)
    #rotate motor of vaccine B
    elif (int(payloadData) == 3):
        print("bye")
        p2.ChangeDutyCycle(7.5)
        time.sleep(.5)
        p2.ChangeDutyCycle(5)
        time.sleep(.5)
        p2.ChangeDutyCycle(2.5)
        time.sleep(5)
        p2.ChangeDutyCycle(5)
        time.sleep(.5)
        p2.ChangeDutyCycle(7.5)
        time.sleep(.5)
    #rotate both motors of vaccine for restocking
    elif (int(payloadData) == 4):
        print("tye")
        p.ChangeDutyCycle(2.5)
        time.sleep(.5)
        p.ChangeDutyCycle(5)
        time.sleep(.5)
        p.ChangeDutyCycle(7.5)
        time.sleep(5)
        p.ChangeDutyCycle(5)
        time.sleep(.5)
        p.ChangeDutyCycle(2.5)
        time.sleep(.5)
        p2.ChangeDutyCycle(7.5)
        time.sleep(.5)
        p2.ChangeDutyCycle(5)
        time.sleep(.5)
        p2.ChangeDutyCycle(2.5)
        time.sleep(5)
        p2.ChangeDutyCycle(5)
        time.sleep(.5)
        p2.ChangeDutyCycle(7.5)
        time.sleep(.5)
    else:
        p.stop()
        p2.stop()
client = mqtt.Client("qq")
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()
