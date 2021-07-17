import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time


pir_light = 27 #pir

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # to disable GPIO warnings at run time
GPIO.setup(pir_light,GPIO.OUT)


MQTT_SERVER = "192.168.0.106"
MQTT_PATH = "set_light"

#connect to the broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    client.subscribe(MQTT_PATH)

#recieve message
def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))


    payloadData = msg.payload.decode('utf-8')
    payloadDataValues = payloadData
        
#    print(payloadDataValues)
    #switch on the lights
    if (int(payloadData) == 1):
        GPIO.output(pir_light,True)
        time.sleep(1.6667)
        GPIO.output(pir_light,False)
    else:
        GPIO.output(pir_light,False)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()
