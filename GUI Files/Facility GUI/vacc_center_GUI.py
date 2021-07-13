import tkinter as tk
from user_message import message_send,play
from PIL import Image, ImageTk

def send_msg ():  
    x1 = entry1.get()

    message_send(x1)

def play_msg():
    play()
    
root= tk.Tk()
root.configure(bg='#D35400')
    

canvas1 = tk.Canvas(root, width = 1630, height = 800, bg = "#D35400")
canvas1.pack()

image5 = Image.open("user_back.png")
image5 = image5.resize((870,460), Image.ANTIALIAS)
test5 = ImageTk.PhotoImage(image5)
label5 = tk.Label(image=test5,bg="black",border = 0)
label5.image = test5
label5.place(x=375, y=10)


image8 = Image.open("play.png")
image8 = image8.resize((170,160), Image.ANTIALIAS)
photo8 = ImageTk.PhotoImage(image8)



b8 = tk.Button(root, image=photo8,bg="black",fg="orange",border = 0,command = play_msg)
b8.place(x=1050, y=500)


entry1 = tk.Entry (root,width = 100) 
canvas1.create_window(700, 540, window=entry1)
  
    
button1 = tk.Button(text='Click here to send', command=send_msg,width=22,height=2)
canvas1.create_window(710, 620, window=button1)


root.mainloop()
