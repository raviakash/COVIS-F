import paho.mqtt.client as mqttClient
import time
import xlrd
from datetime import datetime
import pandas as pd
from xlwt import Workbook

def on_connect1(client, userdata, flags, rc):
  
    if rc == 0:  
        print("Connected to broker sub")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")
        


def on_message(client, userdata, msg):
    
    global i
    
    value = msg.payload.decode('utf-8')
    j,temp=value.split(",")
 
    print(temp)
    i = i + 1

    #--------- Accessing the System Time ---------#
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    #--------- Writing to Excel file -------------#
    sheet.write(i,0,current_time)    
    sheet.write(i,1,temp)
    wb.save("temp_data.xls") 



#-------- Creating Excel file for storing value ------#
i = 0
wb = Workbook()
sheet = wb.add_sheet('Sheet 1')
sheet.write(0,0,"Time") 
sheet.write(0,1,"Temperature") 


    
Connected = False   #global variable for the state of the connection
broker_address= "192.168.1.8"               #IP address of broker
port = 1883
user = ""
password = ""

client = mqttClient.Client("sub2")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect1                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker 
client.subscribe("sense_temp")
client.on_message= on_message

client.loop_forever()
