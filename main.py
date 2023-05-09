from tkinter import *
import pyscreenrec

root = Tk()
root.geometry("500x600")
root.title("Screen recorder")
root.config(bg="#fff")
root.resizable(False,False)

def start_rec():
    file = Filename.get()
    rec.start_recording(str(file+".mp4"),5)

def pause_rec():
    rec.pause_recording()
def ruseme_rec():
    rec.resume_recording()
def stop_rec():
    rec.stop_recording()
    


rec = pyscreenrec.ScreenRecorder()

photo = PhotoImage(file = "ic.png")
root.iconphoto(False, photo)

image1 = PhotoImage(file="ic.png")
Label(root, image=image1, bg="#fff").place(x=-190, y=20)
lbl = Label(root,text="Screen recorder" , bg="#fff", font="arial 15 bold")
lbl.pack(pady=20)

Filename=StringVar()
entry = Entry(root,textvariable=Filename, width=18, font="arial 15")
entry.place(x=100, y= 350)
Filename.set("recoding")
 
start=Button(root,text="Start", font="arial 22", bd=0, command=start_rec)
start.place(x=195,y=270)


image4 = PhotoImage(file = "p.png")
pouse =  Button(root,image=image4, bd=0, bg="#fff", width=90, height=100, command=pause_rec )
pouse.place(x=50, y=470)

image5 = PhotoImage(file = "st1.png")
start1 = Button(root,image=image5, bd=0, bg="#fff", width=100, height=100, command=ruseme_rec)
start1.place(x=200, y=470)

image6 = PhotoImage(file = "cl.png")
cl = Button(root,image=image6, bd=0, bg="#fff", width=100, height=100, command=stop_rec)
cl.place(x=350, y=470)


root.mainloop()
