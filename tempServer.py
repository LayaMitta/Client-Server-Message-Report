import socket   
# import thread module 
from _thread import *
import threading
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
from tkinter import ttk
from time import strftime


import tkinter
import tkinter.messagebox

  
print_lock = threading.Lock() 



    

# thread function 
def threaded(c,x):
    l=[]
    while True: 
        #print_lock.acquire()
        # data received from client 
        data = c.recv(1024)
        data=str(data.decode('ascii'))
        if not data:
            print('Connection with client'+str(x)+' ended') 
              
            # lock released on exit 
            #print_lock.release() 
            break
        
        # reverse the given string from client
        l.append(str(data))
        print("Query from client"+str(x)+":"+str(data))
        data=input("Reply:")
        l.append(data)
        
  
        # send back reversed string to client 
        c.send(data.encode('ascii'))
        #print_lock.release()
        
    # connection closed
    s="Chat of Client:"+str(x)+"\n"
    for i in range(len(l)):
        if(i%2==0):
            s=s+"Server:"+l[i]+"\n"
        else:
            s=s+"Client:"+l[i]+"\n"
    root=Tk()
    root.geometry("150x50")
    root.title("Chat Window")
    
    label1 = Label(root,text="Client"+str(x)+" has disconnected")
    label1.place(x=15,y=15)
    tkinter.messagebox.showinfo("Chat Info",s)
    root.destroy()
    c.close() 
  
  
def Main(): 
    host = "" 
  
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
  
    # a forever loop until client wants to exit
    n=0
    while True:
        
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        #print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1])
        n=n+1
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,n))
        
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 
