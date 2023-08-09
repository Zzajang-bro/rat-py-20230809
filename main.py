import os
from tkinter import filedialog
from tkinter import messagebox

list_file = []                                        
files = filedialog.askopenfilenames(initialdir="/",\
                title = "select your file",\
                filetypes = (("*.xlsx","*xlsx"),("*.xls","*xls"),("*.csv","*csv")))

if files == '':
    messagebox.showwarning("title", "msg")    #if file == ''

print(files)    #files 리스트 값 출력
