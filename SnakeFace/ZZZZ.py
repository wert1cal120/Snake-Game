import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Image')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

python_image = tk.PhotoImage(file=r'C:\Users\werti\PycharmProjects\SnakeGame\SnakeFace\face_r.png')
canvas.create_image(
    (100, 100),
    image=python_image
)


root.mainloop()