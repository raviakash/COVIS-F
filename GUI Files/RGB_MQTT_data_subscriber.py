import paho.mqtt.client as mqttClient
import time
import xlrd
import pandas as pd
from xlwt import Workbook
from datetime import datetime
import smtplib
import sys

def on_connect(client, userdata, flags, rc):
  
    if rc == 0:  
        print("Connected to broker sub")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
    else:
        print("Connection failed")
        

def on_message(client, userdata, msg):
    
    global i,j,pfizer,moderna,entry


    stock = msg.payload.decode('utf-8')
    

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    #----- Pfizer Vaccine-------#
    if((stock) == "green"):
       
        #print("Room 1")
        i = i + 1
        pfizer = pfizer - 2
        sheet.write(i,0,current_time)    
        sheet.write(i,1,pfizer)    
        sheet.write(i,2,moderna)
        print(pfizer)
        print(moderna)
        
    #----- Moderna Vaccine-------#

    elif((stock) == "red"):
       
        #print("Room 2")
        i = i + 1
        moderna = moderna - 2
        sheet.write(i,0,current_time)    
        sheet.write(i,1,pfizer)
        sheet.write(i,2,moderna)
        print(pfizer)
        print(moderna)

    #----- Restocking Vaccine-------#
        
    elif((stock) == "blue"):
        pfizer = 10
        moderna = 10
        i = i + 1
        sheet.write(i,0,current_time)    
        sheet.write(i,1,pfizer)
        sheet.write(i,2,moderna)
        print(pfizer)
        print(moderna)

    #----- Notifying through Email -------#
    
    if((pfizer < 5) or (moderna <5)):
        gmail_user = 'covisfacility@gmail.com'
        gmail_password = 'aiihaiih890890'
        pf= pfizer
        mo= moderna
        sent_from = gmail_user
        to = ['adityakrishna.okade@gmail.com', 'aditya.okade@gmail.com']
        subject = 'Notification: Vaccine Restock Reminder'
        body = 'Please restock the vaccine stock. Currently one or more vaccines are under the defined limit.'+"\n"+"Stocks remaining... "+"\n"+"Pfizer vaccine stock = "+str(pf)+"\n"+"Moderna vaccine stock ="+str(mo)
        email_text = """\
        From: %s
        To: %s
        Subject: %s

        %s
        """ % (sent_from, ", ".join(to), subject, body)
        

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(gmail_user, gmail_password)
            smtp_server.sendmail(sent_from, to, email_text)
            smtp_server.close()
            print ("Email sent successfully!")
        except Exception as ex:
            print ("Something went wrong….",ex)
            

    wb.save("stock_count.xls")

i = 1
pfizer = 10
moderna = 10

#------- Creating Excel file and storing value in it ---------#
wb = Workbook()
sheet = wb.add_sheet('Sheet 1')
sheet.write(0,0,"Time") 
sheet.write(0,1,"Pfizer")
sheet.write(0,2,"Moderna")

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
sheet.write(i,0,current_time)    
sheet.write(i,2,moderna)
sheet.write(i,1,moderna)

Connected = False   #global variable for the state of the connection
broker_address= "192.168.1.8"
port = 1883
user = ""
password = ""

client = mqttClient.Client("sub1")                #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker 
client.subscribe("sense_rgb")                       #subscribed topic
client.on_message= on_message

client.loop_forever()
