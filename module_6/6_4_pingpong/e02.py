import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITTLE = "Ping Pong"

class Game(arcade.Window):
    def on_activate(self):
        self.clear((255, 255, 255))
    

if __name__ == "__main__":
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITTLE)
    arcade.run

