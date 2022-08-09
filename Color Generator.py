# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 10:33:39 2022

@author: ishar
"""

from tkinter import *
import random
root = Tk()
root.title("Encapsulation")
root.geometry("500x400")
root.config(bg="white")

label_name = Label(root,font=("Arial",40),bg="white")
label_name.place(relx=0.5,rely=0.3, anchor= CENTER)


class game:
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["BLACK","PINK","GREEN","BLUE","YELLOW","RED"]
        self.random_number_for_text = random.randint(0,5)
        self.color = ["black","pink","green","blue","yellow","red"]
        self.random_number_for_color = random.randint(0,5)
        label_name["text"] =  self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]
        
obj=game()
btn=Button(root, text="Start", command=obj.updateGame, bg="blue",fg="white", padx=20, pady=20, relief=FLAT, font=("Arial",15))
btn.place(relx=0.5, rely=0.6, anchor=CENTER)
root.mainloop()