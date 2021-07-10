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
    

    temp = msg.payload.decode('utf-8')
    print(temp)

    domainfile = "covis_storagedomain.pddl"

    #----- ROOM-1-------#
    if( float(temp) >= 35 ):
       
        print("Room temp high")
        problemfile = "tempsense.pddl"


        data = {'domain': open(domainfile, 'r').read(),
            'problem': open(problemfile, 'r').read()}

        response = requests.post('http://solver.planning.domains/solve', json=data).json()

        actresult = []
        
        for act in response['result']['plan']:
           step = act['name']
           actuations = step[1:len(step)-1].split(' ')
           actresult.append(actuations)

        
        if 'tempc' in str(actresult):
            print('Reducing temperature')
            data = "5"
            client.publish("set_temp",data)
        actresult.clear()   
        
    else:
            data = "0"
            client.publish("set_temp",data)
        
        


    
Connected = False   #global variable for the state of the connection
broker_address= "192.168.0.106"
port = 1883
user = ""
password = ""

client1 = mqttClient.Client("temp_sub")               #create new instance
client1.username_pw_set(user, password=password)    #set username and password
client1.on_connect= on_connect1                      #attach function to callback
client1.connect(broker_address, port=port)          #connect to broker 
client1.subscribe("sense_temp")
client1.on_message= on_message

client2 = mqttClient.Client("temp_pub")               #create new instance
client2.username_pw_set(user, password=password)    #set username and password
#client2.on_connect= on_connect1                     #attach function to callback
client2.connect(broker_address, port=port)          #connect to broker 

#client2.on_message= on_message1

client1.loop_forever()
