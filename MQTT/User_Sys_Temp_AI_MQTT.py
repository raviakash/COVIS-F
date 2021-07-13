import paho.mqtt.client as mqttClient
import time
import requests
import tkinter as tk

def on_connect(client, userdata, flags, rc):
  
    if rc == 0:  
        print("Connected to broker sub")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")
        

def on_message(client, userdata, msg):

    global entry,user_temp,sys_temp
    value = msg.payload.decode('utf-8')
    i,temp=value.split(",")
    print(i,temp)
    domainfile = "covis_storagedomain.pddl"

    if(int(i) == 1):
        entry = True
    else:
        sys_temp=float(temp)
        
    if(entry):
        if(int(i)==1):
            user_temp = float(temp)
        else:
            sys_temp = float(temp)
            
        diff = user_temp - sys_temp
        print(user_temp,diff)
        if(abs(diff)>2):
                    
            if(user_temp<sys_temp):   
                  data = 5
                  client.publish("set_temp",data)
            if(user_temp>sys_temp):
                  data = 0
                  client.publish("set_temp",data)

        else:
            entry = False
            data = 0
            client.publish("set_temp",data)

            
    elif( float(sys_temp) >= 27):
       
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

    print("")
user_temp = 22
sys_temp = 28
entry = False
    
Connected = False   #global variable for the state of the connection
broker_address= "192.168.0.107"
port = 1883
user = ""
password = ""
client1 = mqttClient.Client("temp_sub")               #create new instance
client1.username_pw_set(user, password=password)    #set username and password
client1.on_connect= on_connect                     #attach function to callback
client1.connect(broker_address, port=port)          #connect to broker 
client1.subscribe("sense_temp")
client1.on_message= on_message
    
client2 = mqttClient.Client("temp_pub")               #create new instance
client2.username_pw_set(user, password=password)    #set username and password
client2.connect(broker_address, port=port)          #connect to broker 

client1.loop_forever()
