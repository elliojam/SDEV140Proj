# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 18:25:53 2025

@author: ellio
"""

import tkinter as tk


class appwindow(tk.Tk):
    
    def mainwindow(root):
        root.geometry('500x600')
        root.resizable(width = True, height = True)
        root.title('Hello App')
        root.configure(background='gray')
    
    def buttonprint(root):
        root.counter+=1
        for widget in root.grid_slaves(0,0): #root.winfo_children selects everything
            widget.destroy()
        label1 = tk.Label(root, text = f'{root.counter}',font=('Arial',100))
        label1.grid(row=0, column=0,sticky='NEWS')
        for widget in root.grid_slaves(0,1):
            widget.destroy()
        
        label2 = tk.Label(root, text = f'{root.textfield.get()}',font=('Wingdings',60))
        label2.grid(row=0, column=1,sticky='WE')
    
    def __init__(root):
        super().__init__()
        root.mainwindow()
        
        label1 = tk.Label(root, text = '0',font=('Arial',100))
        label1.grid(row=0, column=0,sticky='NEWS')
        
        label2 = tk.Label(root, text = '2',font=('Comic Sans MS',60))
        label2.grid(row=0, column=1,sticky='WE')
        
        label3 = tk.Label(root, text = '3',font=('Comic Sans MS',20))
        label3.grid(row=1, column=0,sticky='NS')
        
        label5 = tk.Label(root, text = '5',font=('Arial',75))
        label5.grid(row=0, column=2,sticky='NSW', rowspan=2)
        
        # root.cat_image = tk.PhotoImage(file = 'cat.png')
        # tk.Label(root, image = root.cat_image).grid(row=3, column=0,rowspan=3)
        
        button1 = tk.Button(root,command=root.buttonprint,text='Button',font=('Papyrus',55))
        button1.grid(row=3, column=0,sticky='NESW',columnspan=3)
        
        root.counter = 0
        root.textfield = tk.Entry(root)
        root.textfield.grid(row=1, column=1,padx=20)
        
def main():
    appwindow().mainloop()
    
if __name__ == "__main__":
    main()