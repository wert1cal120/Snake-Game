import tkinter as tk
import random as rand


class Game:
    def __init__(self, master, map_size):
        self.map_size = map_size
        self.canvas = tk.Canvas(master, width=self.map_size, height=self.map_size, bg='#aad751')
        self.canvas.pack()
        self.MapBuiulder()

        #              x    y   x   y  |  x    y   x  y |  x    y   x   y
        self.snake = [[20, 20, 40, 40], [40, 20, 60, 40], [60, 20, 80, 40]]
        self.snake_rectangles = []
        self.Snake()

        self.apple = []
        self.picked_apples = 0
        self.apple_counter = tk.Label(master, text=self.picked_apples)
        self.apple_counter.pack()
        self.Apple()
        self.face_pics = {'r': tk.PhotoImage(file=r'SnakeFace\face_r.png'),
                          'u': tk.PhotoImage(file=r'SnakeFace\face_u.png'),
                          'l': tk.PhotoImage(file=r'SnakeFace\face_l.png'),
                          'd': tk.PhotoImage(file=r'SnakeFace\face_d.png')}
        self.face = self.canvas.create_image(70, 30, image=self.face_pics['r'])

    def MapBuiulder(self):
        for i in range(0, self.map_size + 1, 40):
            for j in range(0, self.map_size + 1, 40):
                self.canvas.create_rectangle(i, j, i + 20, j + 20, fill='#a2d149', outline="")
        for i in range(20, self.map_size + 1, 40):
            for j in range(20, self.map_size + 1, 40):
                self.canvas.create_rectangle(i, j, i + 20, j + 20, fill='#a2d149', outline="")

    def Snake(self):
        if len(self.snake_rectangles) == 0:
            for i in self.snake:
                self.snake_rectangles.append(self.canvas.create_rectangle(*i, fill="#447ed5", outline=""))
        else:
            self.snake_rectangles.append(self.canvas.create_rectangle(*self.snake[-1], fill="#447ed5", outline=""))

    def Apple(self):
        x, y = self.NSC(rand.randint(0, self.map_size - 20 + 1)), self.NSC(rand.randint(0, self.map_size - 20 + 1))

        if [x, y, x + 20, y + 20] in self.snake:
            return self.Apple()

        self.apple.append(self.canvas.create_oval(x, y, x + 20, y + 20, fill="red", outline=""))
        self.apple.append([x, y, x + 20, y + 20])

    def CheckPosition(self):
        if self.snake.count(self.snake[-1]) > 1:
            master.unbind('<Key>', bind_id)
            self.GameOver()
            return 1

            # apple
        if self.snake[-1] == self.apple[1]:
            self.canvas.delete(self.apple[0])
            self.apple.clear()
            self.Apple()
            self.picked_apples += 1
            self.apple_counter.config(text=self.picked_apples)

        else:
            self.canvas.delete(self.snake_rectangles[0])
            self.snake.pop(0)
            self.snake_rectangles.pop(0)

        if (x := max(self.snake[-1])) > self.map_size:
            self.snake[-1][self.snake[-1].index(x) - 2] = x - self.map_size - 20
            self.snake[-1][self.snake[-1].index(x)] = x - self.map_size

        if (x := min(self.snake[-1])) < 0:
            self.snake[-1][self.snake[-1].index(x) - 2] = x + self.map_size + 20
            self.snake[-1][self.snake[-1].index(x)] = x + self.map_size

    def Face(self, direction):
        self.canvas.delete(self.face)
        self.face = self.canvas.create_image(self.snake[-1][0] + 10, self.snake[-1][1] + 10,
                                             image=self.face_pics[direction])

    def Update(self, direction):
        # snake
        x, y, z = 0, 0, ''
        rectangle = self.snake[-1]
        match direction.keycode:
            case 37:  # Left
                x -= 20
                z = 'l'
            case 38:  # Up
                y -= 20
                z = 'u'
            case 39:  # Right
                x += 20
                z = 'r'
            case 40:  # Down
                y += 20
                z = 'd'
            case _:
                return

        self.snake.append([rectangle[0] + x, rectangle[1] + y, rectangle[2] + x, rectangle[3] + y])
        if self.CheckPosition() is not None:
            return
        self.Snake()
        self.Face(z)

    def GameOver(self):
        self.canvas.create_oval(self.map_size / 2 - 80, self.map_size / 2 - 40, self.map_size / 2 + 80,
                                self.map_size / 2 + 40, fill="black", outline='white')
        self.canvas.create_text(self.map_size / 2, self.map_size / 2, text='Game Over', fill='red')

    def NSC(self, number):
        if number % 20 == 0:
            return int(number)
        else:
            return self.NSC(number - 1)


def StartGame(map_size = 400):
    master = tk.Tk()
    map_size = map_size

    game = Game(master, map_size)

    # master config
    master.geometry(f'{map_size}x{map_size + 50}')
    bind_id = master.bind('<Key>', lambda x: game.Update(x))
    master.mainloop()

if __name__ == '__main__':
    StartGame(400)
