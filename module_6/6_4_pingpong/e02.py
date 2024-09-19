import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITTLE = "Ballgame"


# import os
# print(os.getcwd())


class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__("module_6/6_4_pingpong/bar_with.png", 0.5)

class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__("module_6/6_4_pingpong/yellowball.png", 0.06)


class Game(arcade.Window):
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bar = Bar()
        self.ball = Ball()
        self.setup()

    def on_draw(self):
        self.clear((255, 255, 255))
        self.bar.draw()
        self.ball.draw()

    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
    

if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITTLE)
    arcade.run()

