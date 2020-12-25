import tkinter as tk
from tkinter import filedialog, Text, messagebox
import os
from functools import partial

root=tk.Tk()
apps =[]



def get_name(path):
    fp=path.split('/')
    fn=fp[-1]
    fn=fn.split('.')
    return fn[0]



if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps=f.read()
        tempApps= tempApps.split(',')
        apps=[x for x in tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/", title="Select File", 
        filetypes=(("executables","*.exe"), ("all files", "*.*")))
    apps.append(get_name((filename)))

    for app in apps:
        button=tk.Button(frame, text=app, command=partial(removeapp,app))
        button.pack()

def resetApp():
    apps=[]
    for widget in frame.winfo_children():
        widget.destroy()
    
    for app in apps:
        button=tk.Button(frame, text=app,command=partial(removeapp,app))
        button.pack()

def runApps():
    for app in apps:
        os.startfile(app)

def removeapp(prog):
    for widget in frame.winfo_children():
        widget.destroy()
    for app in apps:
        if prog==app:
            apps.remove(app)
    for app in apps:
        button=tk.Button(frame, text=app, command=partial(removeapp,app))
        button.pack()

def callback_remove(prog):
    ans=messagebox.askyesno("Erase app", "Are you sure you would like to erase {} from the list?".format(prog))
    if ans==True:
        removeapp(prog)

canvas=tk.Canvas(root,height=800, width=800, bg="#add8e6")
canvas.pack()

frame=tk.Frame(root, bg="white")
frame.place(relwidth=0.8,relheight=0.8, relx=0.1,rely=0.1)

openfile=tk.Button(root,text="Open File", padx=10,pady=10, fg="white", bg="#263D42", command=addApp)
openfile.pack()
runapps=tk.Button(root,text="Run apps", padx=10,pady=10, fg="white", bg="#263D42", command=runApps)
runapps.pack()
k=[]

for app in apps:
    k.append(app)
    #img=get_icon(app,'small')
    k[-1]=tk.Button(frame, text=app,command=partial(callback_remove,app))
    k[-1].pack()
    print(k[-1])



root.iconbitmap('assets\\test_icon.ico')
root.mainloop()

with open('save.txt','w') as f:
    for app in apps:
        f.write(app+',')

