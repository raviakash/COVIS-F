import tkinter as tk
import plotly
import plotly.graph_objects as go
import pandas as pd
from tkinter import *
from publisher_manager_GUI import *
from PIL import Image, ImageTk
import os
from plotly.subplots import make_subplots
  


def people_count():  
    excel_file = 'vaccinated_count.xls'
    df = pd.read_excel(excel_file)
    print(df)
    data1 = [go.Scatter( x=df['Time'],y=df['People_Vaccinated'],marker = {'color' : 'orange'})]
    fig1 = go.Figure(data1,layout=go.Layout(title=go.layout.Title(text="Count of Vaccinated People")))
    plotly.offline.plot(fig1, filename="vaccinated_people_time.html")


    data2 = go.Pie( labels=df['Time_slot'],values=df['Count'])
    
    fig2 = go.Figure(data2,layout=go.Layout(title=go.layout.Title(text="Count of Vaccinated People")))  

    #colors = ['mediumturquoise',  'darkorange', 'gold']
    colors = ['#bc5090',  '#58508d', '#ff6361']

    fig2.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=40,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))

    plotly.offline.plot(fig2, filename="vaccinated_people.html")



def room_temp():  
    excel_file = 'temp_data.xls'
    df = pd.read_excel(excel_file)
    print(df)
    data1 = [go.Scatter( x=df['Time'],y=df['Temperature'],marker = {'color' : 'red'})]
    fig1 = go.Figure(data1,layout=go.Layout(title=go.layout.Title(text="Room1 Temperature")))
    plotly.offline.plot(fig1, filename="room_temperature.html")


def vaccin_stock():  
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    excel_file = 'stock_count.xls'
    df = pd.read_excel(excel_file)
    print(df)

    fig.add_trace(
    go.Scatter(x=df['Time'],y=df['Pfizer'], name = "Pfizer"),
    secondary_y=False,
    )

    fig.add_trace(
    go.Scatter(x=df['Time'],y=df['Moderna'], name="Moderna")
    )

    fig.update_layout(
    title_text="Vaccine Stack Used "
    )
    fig.update_xaxes(title_text="<b>Time</b>")
    fig.update_yaxes(title_text="<b>Temperature</b>", secondary_y=False)
    plotly.offline.plot(fig, filename="vaccine_stocks.html")

def alarm():  
    print(1+2)
    aalarm()

def room1():
   a = "1"
   selection = str(var1.get())
   print(selection)
   slider(a,selection)
   
def room2():
   a = "1"
   selection = str(var2.get())
   print(selection)
   slider(a,selection)

def voice_msg():  
    os.system("user_msg.mp3")

def send_msg ():  
    x1 = entry1.get()
    print(x1)
    message_send(x1)
    
# --- main ---

# init    
root = tk.Tk()
root.configure(bg='black')

var1 = DoubleVar()
var2 = DoubleVar()



# load image


image = Image.open("db11.png")
image = image.resize((180,170), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image)

image = Image.open("db22.png")
image = image.resize((180,170), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image)

image = Image.open("db33.png")
image = image.resize((180,170), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image)

image = Image.open("stop.png")
image = image.resize((110,130), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(image)

image = Image.open("radio.png")
image = image.resize((220,160), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(image)


image = Image.open("back2.png")
test = ImageTk.PhotoImage(image)
label1 = tk.Label(image=test)
label1.image = test

# button with image binded to the same function 

b1 = tk.Button(root, image=photo1,bg="black",border = 0,command = people_count)
b1.place(x=100, y=650)

b2 = tk.Button(root, image=photo2,bg="black",fg="black",border = 0,command = room_temp)
b2.place(x=440, y=650)

b3 = tk.Button(root, image=photo3,bg="black",fg="black",border = 0,command = vaccin_stock)
b3.place(x=840, y=650)

b4 = tk.Button(root, image=photo4,bg="black",fg="black",border = 0,command = alarm)
b4.place(x=250, y=350)

b5 = tk.Button(root, image=photo5,bg="black",fg="black",border = 0,command = voice_msg)
b5.place(x=600, y=350)

b6 = tk.Button(root,text="SEND",bg="green",fg="black",border = 0,command = room1)
b6.place(x=1245, y=605)

b7 = tk.Button(root,text="SEND",bg="green",fg="black",border = 0,command = room2)
b7.place(x=1445, y=605)


# Imporintg Images and resizing
image = Image.open("back2.png")
image = image.resize((800,230), Image.ANTIALIAS) 
test1 = ImageTk.PhotoImage(image)
label1 = tk.Label(image=test1,bg="black",border = 0)
label1.image = test1
label1.place(x=370, y=0)

image = Image.open("corner2.png")
image = image.resize((450,270), Image.ANTIALIAS)
test2 = ImageTk.PhotoImage(image)
label2 = tk.Label(image=test2,bg="black",border = 0)
label2.image = test2
label2.place(x=0, y=0)

image = Image.open("dcorner2.png")
image = image.resize((450,270), Image.ANTIALIAS)
test3 = ImageTk.PhotoImage(image)
label3 = tk.Label(image=test3,bg="black",border = 0)
label3.image = test3
label3.place(x=1150, y=570)

image = Image.open("dataanalysis.png")
test4 = ImageTk.PhotoImage(image)
label4 = tk.Label(image=test4,bg="black",border = 0)
label4.image = test4
label4.place(x=410, y=500)

image = Image.open("counttxt.png")
test5 = ImageTk.PhotoImage(image)
label5 = tk.Label(image=test5,bg="black",border = 0)
label5.image = test5
label5.place(x=50, y=580)

image = Image.open("temptxt.png")
test6 = ImageTk.PhotoImage(image)
label6 = tk.Label(image=test6,bg="black",border = 0)
label6.image = test6
label6.place(x=380, y=580)

image = Image.open("stacktext.png")
test7 = ImageTk.PhotoImage(image)
label7 = tk.Label(image=test7,bg="black",border = 0)
label7.image = test7
label7.place(x=750, y=580)

image = Image.open("tempslide.png")
test8 = ImageTk.PhotoImage(image)
label8 = tk.Label(image=test8,bg="black",border = 0)
label8.image = test8
label8.place(x=1200, y=260)

image = Image.open("stoptxt.png")
test9 = ImageTk.PhotoImage(image)
label9 = tk.Label(image=test9,bg="black",border = 0)
label9.image = test9
label9.place(x=150, y=300)

image = Image.open("voicemsg.png")
test10 = ImageTk.PhotoImage(image)
label10 = tk.Label(image=test10,bg="black",border = 0)
label10.image = test10
label10.place(x=520, y=300)

image = Image.open("send_msg.png")
test11 = ImageTk.PhotoImage(image)
label11 = tk.Label(image=test11,bg="black",border = 0)
label11.image = test11
label11.place(x=850, y=300)

canvas1 = tk.Canvas(root, width = 205, height = 25, bg = "black")
canvas1.place(x=900,y=420)
entry1 = tk.Entry (root,width =30) 
canvas1.create_window(100, 13, window=entry1)
button11 = tk.Button(text='Click here to send', command=send_msg,width=12,height=1)
button11.place(x=960,y=470)


#Sliders for temperature control

w1 = Scale(root,label='TEMP.',
            variable = var1,
            from_=-20 , to=40,
            length=260,
            tickinterval=4,
            orient=VERTICAL,
            bg="black",
            fg="white",
            troughcolor="blue",
            width=20)
w1.place(x=1200,y=340)

w2 = Scale(root,label='TEMP.',
            variable = var2,
            from_=-20 , to=20,
            length=260,
            tickinterval=4,
            orient=VERTICAL,
            bg="black",
            fg="white",
            troughcolor="blue",
            width=20)
w2.place(x=1400,y=340)
