#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#import the whole module
from tkinter import*


# In[ ]:


class Currency_converter():
    def __init__(self):
        window=Tk()  # Create application window  
        window.title('Currency Converter')  # Add title to application window
        window.configure(bg='blue')  # Add background color to application window
        
        # Adding Label widgets to application window
        Label(window,font='Calibri',bg='blue',text='Amount to be converted').grid(row=1, column=1, sticky=W)
        Label(window,font='Calibri',bg='blue',text='Conversion rate').grid(row=2, column=1, sticky=W)
        Label(window,font='Calibri',bg='blue',text='Converted amount').grid(row=3, column=1, sticky=W)
       
        # Create objects and add entry functions
        self.amounttoconvertVar=StringVar()
        Entry(window, textvariable=self.amounttoconvertVar, justify='right').grid(row=1, column=2)
        self.conversionrateVar=StringVar()
        Entry(window, textvariable=self.conversionrateVar, justify='right').grid(row=2, column=2)
        self.convertedamountVar=StringVar()
        lblconvertedamount=Label(window, font='Calibri', bg='blue', textvariable=self.convertedamountVar).grid(row=3, column=2, sticky=E)
        
        # Create convert and clear buttons . When clicked they will call their respective functions
        btconvertedamount=Button(window, text='Convert', font='Calibri', bg='red', fg='white', command=self.convertedamount).grid(row=4, column=2, sticky=E)
        btdelete_all=Button(window, text='Clear', font='Calibri', bg='red', fg='white', command=self.delete_all).grid(row=4, column=6, padx=25, pady=25, sticky=E)
        
        window.mainloop()  # Runs the application program
        
   
    # Function to do the conversion. Stores inputs and performs conversion
    def convertedamount(self):
        amt=float(self.conversionrateVar.get())
        convertedamountVar=float(self.amounttoconvertVar.get()) * amt
        self.convertedamountVar.set(format(convertedamountVar, '10.2f'))
        
    # Function to clear inputs
    def delete_all(self):
        self.amounttoconvertVar.set(' ')
        self.conversionrateVar.set(' ')
        self.convertedamountVar.set(' ') 
    
Currency_converter() 


# In[ ]:




