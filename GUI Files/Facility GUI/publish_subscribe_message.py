import paho.mqtt.client as mqttClient
import time
import os
from gtts import gTTS

def on_connect(client, userdata, flags, rc):
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")

def message_send(msg):
    print(msg)
    client.publish("to_mg_message",msg)

def on_message(client, userdata, message):
    global i
    mytext = message.payload.decode('UTF-8')
    print(mytext)
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("manager_msg.mp3")
    os.system("manager_msg.mp3")

def play():
    os.system("manager_msg.mp3")
    
Connected = False   #global variable for the state of the connection
broker_address= "192.168.1.8"
port = 1883
user = ""
password = ""
client = mqttClient.Client("new_user_messager")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker 
client.subscribe("to_user_message")
client.on_message= on_message
client.loop_start()        #start the loop
