# Pomocheco - Pomodoro em python

from logging import root
import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
from playsound import playsound
import time


#Timer  = min*60
timer = 25*60 #Trabalho
timer = 5*60 #Descanso

minuto, segundo = divmod(1366, 60)
print(minuto)
print(segundo)

class Pomocheco:
    def __init__(self, root):
        self.root = root

    
    def desc_trab(self, timer):
        minutos, segundos = divmod(timer, 60)
        self.min.set(f"{minutos:02d}")
        self.seg.set(f"{segundos:02d}")
        self.root.update()
        time.sleep(1)
    

    def trab(self):
        timer = 25*60
        while timer >= 0:
            pomo.desc_trab(timer)
            if timer == 0:
                playsound('/Pomocheco/Sons/Som_Alerta.wav')
                messagebox.showinfo("Bom trabalho, cachorro", "Take A Break, \
                    nClick Break Button")
            timer -=1
    
    def desc(self):
        timer = 5*60
        while timer >= 0:
            pomo.desc_trab(timer)
            if timer == 0:
                playsound('/Pomocheco/Sons/Som_Alerta.wav')
                messagebox.showinfo("Hora de papear!", "Get Back To Work, \
                    nClick Work Button")
            timer -=1

            
    
    # Início do Tkinter
    def main(self):
        PYFORMS_STYLESHEET = 'style.css'
        # Configuração da tela
        self.root.geometry("220x220")
        self.root.resizable(True, True)
        self.root.title("Pomocheco")

        # Label
        self.min = tk.StringVar(self.root)
        self.min.set("25")
        self.seg = tk.StringVar(self.root)
        self.seg.set("00")

        self.min_label = tk.Label(self.root, textvariable=self.min)        
        self.min_label["font"] = ("Arial", "50", "bold")
        self.min_label["background"] = ("Black")
        self.min_label["foreground"] = ("White")   
        self.min_label.place (height=100, width=100, x= 10, y= 10)
        self.seg_label = tk.Label(self.root, textvariable=self.seg)
        self.seg_label["font"] = ("Arial", "50", "bold")
        self.seg_label["background"] = ("Black")
        self.seg_label["foreground"] = ("White")   
        self.seg_label.place (height=100, width=100, x= 110, y= 10)

        # Botões 
   
       
        self.btn_trab = tk.Button(self.root)
        self.btn_trab["font"] = ("Arial", "10", "bold")
        self.btn_trab["width"] = (10)
        self.btn_trab["text"] = "Trabalhar"
        self.btn_trab["command"] = self.trab
        self.btn_trab.place (height=20, width=80, x= 00, y= 150)

        self.bttn_desc = tk.Button(self.root)
        self.bttn_desc["font"] = ("Arial", "10", "bold")
        self.bttn_desc["width"] = (10)
        self.bttn_desc["text"] = "Descansar"
        self.bttn_desc["command"] = self.desc
        self.bttn_desc.place (height=20, width=80, x= 140, y= 150)
        
        self.root.mainloop()
        
if __name__ == '__main__':
    pomo = Pomocheco(tk.Tk())
pomo.main()
