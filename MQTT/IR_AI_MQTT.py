import paho.mqtt.client as mqttClient
import time
import requests

def on_connect1(client, userdata, flags, rc):
  
    if rc == 0:  
        print("Connected to broker sub")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")
        


def on_message(client, userdata, msg):
    

    IR = msg.payload.decode('utf-8')
    print(IR)

    domainfile = "covis_storagedomain.pddl"

    #----- ROOM-1-------#
    if( int(IR) > 9 ):
       
        print("Crowd")
        problemfile = "infrasensered.pddl"

    else:
       
        print("Empty")
        problemfile = "infrasensegreen.pddl"


#    else:
#        problemfile = ""

    data = {'domain': open(domainfile, 'r').read(),
        'problem': open(problemfile, 'r').read()}

    response = requests.post('http://solver.planning.domains/solve', json=data).json()

    actresult = []
    
    for act in response['result']['plan']:
       step = act['name']
       actuations = step[1:len(step)-1].split(' ')
       actresult.append(actuations)
         
    
    if 'lightglowrp' in str(actresult):
        print('Stop inflow')
        data = "0"
        client.publish("set_count",data)

    elif 'lightglowgp' in str(actresult):
        print('Allow people')
        data = "1"
        client.publish("set_count",data)

    actresult.clear()

    
Connected = False   #global variable for the state of the connection
broker_address= "192.168.0.106"
port = 1883
user = ""
password = ""

client1 = mqttClient.Client("IR_sub")               #create new instance
client1.username_pw_set(user, password=password)    #set username and password
client1.on_connect= on_connect1                      #attach function to callback
client1.connect(broker_address, port=port)          #connect to broker 
client1.subscribe("sense_count")
client1.on_message= on_message

client2 = mqttClient.Client("IR_pub")               #create new instance
client2.username_pw_set(user, password=password)    #set username and password
#client2.on_connect= on_connect1                     #attach function to callback
client2.connect(broker_address, port=port)          #connect to broker 

#client2.on_message= on_message1

client1.loop_forever()
