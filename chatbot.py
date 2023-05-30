from tkinter import *

chat = Tk()
chat.title("CHATBOT") 

def send(): 
    message = "You: " + e.get()
    txt.insert(END, message)
    user = e.get().lower()

    if user == "hello": 
        txt.insert(END, "\nBot: Hi\n")
    elif user in ["hi", "hii", "hiiii"]:
        txt.insert(END, "\nBot: Hello\n")
    elif user == "how are you":
        txt.insert(END, "\nBot: Fine! And you?\n")
    elif user in ["fine", "i am good", "i am doing good"]:
        txt.insert(END, "\nBot: Great! How can I help you?\n")
    elif user in ["hey", "heyy"]:
        txt.insert(END, "\nBot: Hi, what's up?\n")
    
    elif user in ["hello siri", "heyy siri"]:
        txt.insert(END, "\nBot: Hi,what I can do for you \n")
    else:
        txt.insert(END, "\nBot: Sorry, I didn't get you.\n")
    
    e.delete(0, END)


txt = Text()
txt.grid(row=0, column=0)

e = Entry(width=100)
e.grid(row=1, column=0)

send = Button(text="Send", command=send)
send.grid(row=1, column=1)

chat.mainloop()