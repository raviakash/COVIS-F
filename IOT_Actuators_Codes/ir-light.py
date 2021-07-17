import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


ir_light = 6  #ir
ir_light2 = 10 #ir2
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # to disable GPIO warnings at run time
GPIO.setup(ir_light,GPIO.OUT)
GPIO.setup(ir_light2,GPIO.OUT)

MQTT_SERVER = "192.168.0.106"
MQTT_PATH = "set_count"

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
    #switch on red LED
    if (int(payloadData) == 0):
        GPIO.output(ir_light,True)
        GPIO.output(ir_light2,False)
    #switch on green LED
    elif (int(payloadData) == 1):
        GPIO.output(ir_light,False)
        GPIO.output(ir_light2,True)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()
