import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")

def aalarm():
    msg = "System Emergency, Please stop all the process"
    print(msg)
    client.publish("to_user_message",msg)

def slider(a,n):
    c = "1"+','+n
    client.publish("sense_temp",c)
    print("mmmm")

def message_send(msg):
    print(msg)
    client.publish("to_user_message",msg)
    
Connected = False   #global variable for the state of the connection
print("bandee")
broker_address= "192.168.1.8"                       #IP address of the broker
port = 1883                                         #default port for MQTT
user = ""
password = ""
client = mqttClient.Client("Publisher_GUI")        #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker 
client.loop_start()                                #start the loop

