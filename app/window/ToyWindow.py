from tkinter import *
from tkinter import messagebox as MessageBox
import subprocess
import os

server_process = None
client_process = None
server_script = os.path.abspath("../app/server/ToyServer.py")
Cclient_script = os.path.abspath("../app/ToyClient.py")
def btn_upDown():
    global server_process
    state=str(btn_upDown.cget("text"))
    if state=="On":     
        server_process = subprocess.Popen(["python",server_script])
        btn_upDown.configure(text="Off")
    else:
        if server_process:
            btn_upDown.configure(text="On")
            server_process.terminate()
            server_process=None
            
def btn_ToyConsole():
    global client_process
    state = str(btn_upDown.cget("text"))
    if state == "Off":
        if os.name == 'nt':  # Windows
            path = r"C:/Users/SANTIAGO/Documents/ToyManagementSQL/app"  
            client_process = subprocess.Popen(["cmd", "/K", f"cd /d {path}"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        else:  #Unix-like
            path = "C:/Users/SANTIAGO/Documents/ToyManagementSQL"  
            client_process = subprocess.Popen(['x-terminal-emulator', '-e', 'sh', '-c', f'cd {path}; exec bash'])
    else:
        MessageBox.showinfo("Error", "Please up the server")



main_window=Tk()
main_window.title("Sever")
main_window.minsize(width=300,height=300)
main_window.config(padx=35,pady=35)
lbl_Tittle=Label(text="ToySQL Server",font=("Arial",15))
lbl_Tittle.grid(column=0,row=1)
lbl_upDown=Label(text="Sever",font=("Arial",11))
lbl_Wclient=Label(text="Web client",font=("Arial",11))
lbl_Cclient=Label(text="Console client",font=("Arial",11))
lbl_upDown.grid(column=0,row=8)
lbl_Wclient.grid(column=0,row=16)
lbl_Cclient.grid(column=0,row=24)
btn_upDown=Button(text="On",font=("Arial",11),command=btn_upDown)
btn_Wclient=Button(text="Open",font=("Arial",11))
btn_Cclient=Button(text="Open",font=("Arial",11),command=btn_ToyConsole)
btn_upDown.grid(column=5,row=8)
btn_Wclient.grid(column=5,row=16)
btn_Cclient.grid(column=5,row=24)



main_window.mainloop()