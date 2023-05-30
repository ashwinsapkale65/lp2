from tkinter import *

chat = Tk()
chat.title('Chatbot')


def send():
    message = "You:" + e.get()
    text.insert(END,message)
    user = e.get().lower()
    
    if user == "hello":
        text.insert(END,"\nBot: hii\n")
        
    e.delete(0,END)
    
e = Entry(width=100)
e.grid(column=1,row=1)

text = Text()
text.grid(column=0,row=0)

send = Button(text="send",command=send)
send.grid(column=1,row=1)
chat.mainloop()