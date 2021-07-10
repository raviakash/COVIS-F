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
        
def on_connect2(client, userdata, flags, rc):
    if rc == 0:
 
        print("Connected to broker pub")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")


def on_message(client, userdata, msg):
    
    global entry
    entry = False


    sensegreen = msg.payload.decode('utf-8')
    print(sensegreen)

    domainfile = "covis_storagedomain.pddl"

    #----- ROOM-1-------#
    if((sensegreen) == "green"):
       
        #print("Room 1")
        problemfile = "greensense.pddl"
        entry = True
    #----- ROOM-2-------#
    elif((sensegreen) == "red"):
       
        #print("Room 2")
        problemfile = "redsense.pddl"
        entry = True
    #----- Vaccine Renewal-------#
    elif((sensegreen) == "blue"):
       
        #print("Vaccine Stack Renewed")
        problemfile = "bluesense.pddl"
        entry = True
#    else:
#        print("banth noda")
#        problemfile = ""
    if(entry):
        data = {'domain': open(domainfile, 'r').read(),
            'problem': open(problemfile, 'r').read()}

        response = requests.post('http://solver.planning.domains/solve', json=data).json()

        actresult = []
        
        for act in response['result']['plan']:
           step = act['name']
           actuations = step[1:len(step)-1].split(' ')
           actresult.append(actuations)
             

        if 'rgbsensegreenp' in str(actresult):
            #print('send green')
            data = "3"
            print(data)            
            client.publish("room_motor",data)

        elif 'rgbsenseredp' in str(actresult):
            data = "2"
            print(data)
            
            client.publish("room_motor",data)

        elif 'rgbsensebluep' in str(actresult):
            data = "4"
            print(data)
            client.publish("room_motor",data)
        else:
            data = "NOT AUTHORISED"
            #client.publish("room_motor",data)

        actresult.clear()


    
Connected = False   #global variable for the state of the connection
broker_address= "192.168.0.106"
port = 1883
user = ""
password = ""

client1 = mqttClient.Client("rgb_sub")               #create new instance
client1.username_pw_set(user, password=password)    #set username and password
client1.on_connect= on_connect1                      #attach function to callback
client1.connect(broker_address, port=port)          #connect to broker 
client1.subscribe("sense_rgb")
client1.on_message= on_message

client2 = mqttClient.Client("rgb_pub")               #create new instance
client2.username_pw_set(user, password=password)    #set username and password
client2.on_connect= on_connect2                      #attach function to callback
client2.connect(broker_address, port=port)          #connect to broker 

#client2.on_message= on_message1

client1.loop_forever()
