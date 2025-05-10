# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 18:25:53 2025

@author: ellio
"""

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tuplerange import myRange

class appwindow(tk.Tk):
    
    def mainwindow(root):
        # Defines Color, Size, Title
        root.geometry('850x450')
        root.resizable(width = True, height = True)
        root.title('Polynomial Graphing')
        root.configure(background='gray')
        
    def errorwindow(root):
        #Creates error window
        errwindow = tk.Toplevel(root)  # Create a new window
        errwindow.title("Error")
        
        # adds image
        root.error_img = tk.PhotoImage(file = 'icon_error.png')
        graph1 = tk.Label(errwindow, image = root.error_img)
        graph1.pack()
        
        # adds label
        label = tk.Label(errwindow, text = root.error, font = ('Arial',18))
        label.pack()
    
    def check_equation(root):
        # Checks if equation is valid, calculates curve
        equation = root.inputbox.get()
        if equation == '':
            # Create error window
            root.error = "Input an equation before graphing!"
            root.errorwindow()
            return None
            
        # Formats equation for python, removes spaces
        equation = equation.replace("^", "**")
        equation = equation.replace(" ","")
        allowed = '1234567890+-*/x()'
        
        openparens = 0 # Used to check if all opened parens close
        
        # Error if invalid chars in input
        for char in equation:
            if char not in allowed:
                # Create error window
                root.error = "You cannot include characters\nother than numbers, math symbols, and x."
                root.errorwindow()
                # End function
                return None
                
            elif char in '(': openparens += 1
            elif char in ')': openparens -= 1
            
        # paren error
        if openparens != 0:
            # Create error window
            root.error = "Parentheses must be balanced\nEach ( must have a )."                
            root.errorwindow()
            # End function
            return None
            
        # Saves equation to root, calculates
        root.equation = equation
        root.calculate_tups()
            
    def calculate_tups(root):
        # Sets axis limits
        try:
            lowbound = float(root.lowbox.get())
            highbound = float(root.highbox.get())
        except:
            # Create error window
            root.error = "Range not possible:\nBoth limits must be numbers."
            root.errorwindow()
            # End function
            return None
        if lowbound >= highbound:
            # Create error window
            root.error = "Range not possible:\nLow bound is greater than high bound."
            root.errorwindow()
            # End function
            return None
        range = highbound - lowbound
        
        # imports equation
        equation = root.equation
        root.xs = myRange(lowbound,highbound,range/100)
        ys = []
        
        # calculates 100 points y values
        for val in root.xs:
            func = []
            prev = ''
            for char in equation:
                if char != 'x':
                    func.append(char)
                elif prev == '*':
                    func.append(f'({str(val)})')
                else:
                    func.append(f'*({str(val)})')
                prev = char
            func = "".join(func)
        
            try:
                y = eval(func)
                ys.append(y)
            except:
                # Create error window
                root.error = "There was an error\nevaluating your equation"
                root.errorwindow()
                # End function
                return None
                
        root.ys = tuple(ys)
        root.graphing()
        
    def graphing(root):
        # Plots graph
        myplot = Figure(figsize = (4,4), dpi = 100)
        ax = myplot.add_subplot(1,1,1)
        ax.plot(root.xs, root.ys)
        ax.grid(True)
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_title("Graph")
        
        try: root.graph1.destroy()
        except: pass
        
        graph = FigureCanvasTkAgg(myplot, master=root)
        graph1 = graph.get_tk_widget()
        graph1.place(x = 5, y = 5)
        graph.draw()
    
    def __init__(root):
        super().__init__()
        root.mainwindow()
        
        root.graph_img = tk.PhotoImage(file = 'graph_img.png')
        
        graph1 = tk.Label(root, image = root.graph_img)
        graph1.place(x = 5, y = 5)
        
        button1 = tk.Button(root,command=root.check_equation,text='Create Graph',font=('Arial',18))
        button1.place(x = 600, y = 150)
        
        root.equation = ''
        root.error = 'Error'
        root.xs = ()
        root.ys = ()
        
        entry_label = tk.Label(root, text = 'Input Equation',font=('Arial',18), bg = "gray")
        entry_label.place(x = 600, y = 70)
        entry_eq = tk.Label(root, text = 'f(x) = ',font=('Arial',18), bg = "gray")
        entry_eq.place(x = 490, y = 100)
        root.inputbox = tk.Entry(root, font = ('Arial',18), width = 20)
        root.inputbox.place(x = 550, y = 100)
        
        low_label = tk.Label(root, text = 'min(x)',font=('Arial',18), bg = "gray")
        low_label.place(x = 550, y = 250)
        root.lowbox = tk.Entry(root, font = ('Arial',18), width = 5)
        root.lowbox.insert(0, '-10')
        root.lowbox.place(x = 550, y = 280)
        
        high_label = tk.Label(root, text = 'max(x)',font=('Arial',18), bg = "gray")
        high_label.place(x = 750, y = 250)
        root.highbox = tk.Entry(root, font = ('Arial',18), width = 5)
        root.highbox.insert(0, '10')
        root.highbox.place(x = 750, y = 280)
        
def main():
    appwindow().mainloop()
    
if __name__ == "__main__":
    main()