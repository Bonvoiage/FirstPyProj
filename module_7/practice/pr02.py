import os
import tkinter

from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Выберите файл",
                                          filetypes = (("Все файлы", "*.*"), ("Текстовые файлы", "*.txt")))
    
    text["text"] = text["text"] + " " + filename
    os.startfile(filename)


w_width = 300
w_height = 120


window = tkinter.Tk()
window.title("проводник")
window.geometry(f"{w_width}x{w_height}")
window.resizable(False, False)
window.config(bg="black")


t_width = 30
t_height = 4
text = tkinter.Label(window, 
                     text="Файл", 
                     height=t_height, 
                     width=t_width, 
                     background="silver")

text.grid(row=1, column=1)
# text.place(x=w_width/4, y=w_height/10)


button_select = tkinter.Button(window, 
                               text="Выбрать файл", 
                               height=2, 
                               width=25,
                               command=file_select)
button_select.grid(row=2, column=1, pady=5)
# button_select.place(x=w_width/4, y=w_height/4)




window.mainloop()

