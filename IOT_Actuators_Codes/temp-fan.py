import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

temp_fan = 21  #fan

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # to disable GPIO warnings at run time
GPIO.setup(temp_fan,GPIO.OUT)


MQTT_SERVER = "192.168.0.106"
MQTT_PATH = "set_temp"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    client.subscribe(MQTT_PATH)


def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))


    payloadData = msg.payload.decode('utf-8')
    payloadDataValues = payloadData

    print(payloadDataValues)
    #switch on fan
    if (int(payloadData) == 5 ):
        GPIO.output(temp_fan,True)
    elif(int(payloadData)== 0):
        GPIO.output(temp_fan,False)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()
