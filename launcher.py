import main as snake
import tkinter as tk

master = tk.Tk()
master.geometry(f'300x400')

value_inside = tk.StringVar(master)
value_inside.set(300)

def StartGame():
    master.destroy()
    snake.StartGame(int(value_inside.get()))

tk.Label(master, text='Snake Game').pack()
tk.Label(master, text='Map Size').pack()
tk.OptionMenu(master, value_inside, *[100, 200, 300, 400, 500, 600] ).pack()
tk.Button(master, text='Start', command=StartGame).pack()

canvas = tk.Canvas(master, width=150, height=150)
canvas.pack()


master.mainloop()