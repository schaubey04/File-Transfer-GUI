from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

shiva=Tk()
shiva.title("Shivam Shareit")
shiva.geometry("450x560+500+200")
shiva.resizable(False,False)
shiva.configure(bg="#f4fdfe")

def Send():
    window=Toplevel()
    window.title("send")
    window.geometry("450x560+500+200")
    window.resizable(False,False)

    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title="Select Image File",
                                            filetypes=(("file_type","*.txt"),("all files","*.*")))

    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host,port))
        s.listen(1)

        print(host)
        print("waiting for any incomming connections...........")

        conn,addr=s.accept()
        file=open(filename,"rb")
        file_data=file.read(1024)
        conn.send(file_data)
        print("Data Has Been Trasnsmitted Successfully...")

    #icon

    send_icon=PhotoImage(file="send.png")
    window.iconphoto(False,send_icon)

    Sbackground=PhotoImage(file="sender.png")
    Label(window,image=Sbackground).place(x=-2,y=0)

    Mbackground=PhotoImage(file="id.png")
    Label(window,image=Mbackground,bg="#f4fdfe").place(x=100,y=260)

    host=socket.gethostname()
    Label(window,text=f"ID: {host}",bg="white",fg="black").place(x=140,y=290)

    Button(window,text="+ select file",width=10,height=1,font=("arial 14 bold"),bg="#fff",fg="#000",command=select_file).place(x=160,y=150)
    Button(window,text="SEND",width=8,height=1,font=("arial 14 bold"),bg="#000",fg="#fff",command=sender).place(x=300,y=150)

    window.mainloop()


def Receive():
    main=Toplevel()
    main.title("receive")
    main.geometry("450x560+500+200")
    main.resizable(False,False)


    def receiver():
        ID=SenderID.get()
        filename1=incomming_file.get()

        s=socket.socket()
        port=8080
        s.connect((ID,port))
        file=open(filename1,"wb")
        file_data=file.recv(1024)
        file.write=(file_data)
        file.close()
        print("File has been received")

    #icon

    receive_icon=PhotoImage(file="receive.png")
    main.iconphoto(False,receive_icon)

    Hbackground=PhotoImage(file="receiver.png")
    Label(main,image=Hbackground).place(x=-2,y=0)

    logo=PhotoImage(file="profile.png")
    Label(main,image=logo,bg="#f4fdfe").place(x=100,y=250)

    Label(main,text="Receive",font=("arial",20),bg="#f4fdfe").place(x=100,y=280)



    Label(main,text="Input Sender Id",font=("arial 10 bold"),bg="#f4fdfe").place(x=20,y=340)
    SenderID= Entry(main,width=25,fg="black",bd=2,bg="white",font=("arial 15"))
    SenderID.place(x=20,y=370)
    SenderID.focus()



    Label(main,text="filename for the incomming file:",font=("arial 10 bold"),bg="#f4fdfe").place(x=20,y=420)
    incomming_file= Entry(main,width=25,fg="black",bd=2,bg="white",font=("arial 15"))
    incomming_file.place(x=20,y=450)

    image_icon=PhotoImage(file="arrow.png")
    rr=Button(main,text="Receive",compound=LEFT,image=image_icon,width=130,bg="#29c790",font="arial 14 bold",command=receiver)
    rr.place(x=20,y=500)







    

    main.mainloop()

#icon

image_icon=PhotoImage(file="icon.png")
shiva.iconphoto(False,image_icon)

Label(shiva,text="File Transfer",font=("Acumin Variable Concept",20,"bold"),bg="#f4fdfe").place(x=20,y=30)

Frame(shiva,width=400,height=2,bg="#f3f5f6").place(x=25,y=80)

send_image=PhotoImage(file="send.png")
send=Button(shiva,image=send_image,bg="#f4fdf6",bd=0,command=Send)
send.place(x=50,y=100)


receive_image=PhotoImage(file="receive.png")
receive=Button(shiva,image=receive_image,bg="#f4fdf6",bd=0,command=Receive)
receive.place(x=300,y=100)

#Label
Label(shiva,text="send",font=("Acumin Variable Concept",17,"bold"),bg="#f4fdfe").place(x=65,y=200)

Label(shiva,text="receive",font=("Acumin Variable Concept",17,"bold"),bg="#f4fdfe").place(x=300,y=200)

background=PhotoImage(file="background.png")
Label(shiva,image=background).place(x=-2,y=320)











shiva.mainloop()