import tkinter as tk
from tkinter import messagebox

def send_message():
    message = entry.get()
    if message:
        chat_display.insert(tk.END, "You: " + message + "\n")
        chatbot_response(message)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Chatbot", "Please enter a message.")

def chatbot_response(message):
    response = "Chatbot: This is a basic chatbot response."
    chat_display.insert(tk.END, response + "\n")

# Create a Tkinter window
window = tk.Tk()
window.title("Chatbot")

# Create a chat display area
chat_display = tk.Text(window, height=20, width=50)
chat_display.pack()

# Create an entry field for user input
entry = tk.Entry(window, width=50)
entry.pack()

# Create a send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Start the Tkinter event loop
window.mainloop()
