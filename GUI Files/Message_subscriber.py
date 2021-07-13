import paho.mqtt.client as mqttClient
from gtts import gTTS
import os

def on_connect(client, userdata, flags, rc):
  
    if rc == 0:  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")
    
def on_message(client, userdata, message):
    global i
    mytext = message.payload.decode('UTF-8')
    print(mytext)

    #--------- Converting text to speech and saving the file----------#
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False) 
    myobj.save("user_msg.mp3")
    os.system("user_msg.mp3")

Connected = False   #global variable for the state of the connection



i = 0
broker_address= "192.168.0.107"  #Broker address
port = 1883                         #Broker port
user = ""                    #Connection username
password = ""            #Connection password
  

client = mqttClient.Client("manager_messager")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                    #attach function to callback
client.connect(broker_address, port=port)          #connect to broker 
client.subscribe("to_mg_message")
client.on_message= on_message
  
client.loop_forever()        #start the loop


