import requests
import time
from tkinter import *

session = requests.Session()
session.trust_env = False
# response = session.get("https://cloud.arest.io/a82023/digital/2/1") #optional 
def on():
    response = session.get("https://cloud.arest.io/xxxxxx/digital/2/0") #
def off():
    response = session.get("https://cloud.arest.io/xxxxxx/digital/2/1")


window= Tk()
window.geometry("500x200")
window.title("Emergency stop window")

B1 = Button(window, text="STOP", width=20, bg="red", fg="black", command=on)
B1.place(x=50,y=90)

B2 = Button(window, text="GET READY", width=20, bg="green", fg="black", command=off)
B2.place(x=250,y=90)

window.mainloop()
