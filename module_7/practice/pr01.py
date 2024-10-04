import tkinter

w_width = 500
w_height = 500



window = tkinter.Tk()
window.title = "проводник"
window.geometry(f"{w_width}x{w_height}")
window.resizable(False, False)
window.config(bg="black")


t_width = 25
t_height = 4
text = tkinter.Label(text="Файл", height=t_height, width=t_width, background="silver")
text.place(x=w_width/4, y=w_height/10)
# text.grid(row=1, column=1)

button_select = tkinter.Button(window, text="Выбрать файл", height=2, width=25)
button_select.place(x=w_width/4, y=w_height/4)

window.mainloop()

