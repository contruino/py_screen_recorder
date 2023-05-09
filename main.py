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
        