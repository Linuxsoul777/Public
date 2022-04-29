from tkinter import *

count = 0
def plus(args):
    global count
    global label
    count += args
    root.config(background="#aed581")
    label.config(background="#aed581")
    label.config(text=count)
    button1.config(background="#ff8a65")
    button2.config(background="#ff8a65")
root = Tk()
root.title("Click me game!")
root.geometry("250x125")
label = Label(root, text="Click the button!")
button1 = Button(root, text="1",command=lambda:plus(1))
button2 = Button(root, text="10",command=lambda:plus(10))
label.pack(pady=10)
button1.pack()
button2.pack()

root.mainloop()
