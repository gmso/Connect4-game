from src.PlayerInput import PlayerInput
from src.Game import Game
from src.ConsoleRenderer import ConsoleRenderer as Renderer


class App():
    """Manage game loop of input -> process -> render."""

    def __init__(self) -> None:
        """Constructor."""
        
        self.input = PlayerInput()
        self.game = Game()
        self.renderer = Renderer()

    def run(self):
        """Game loop."""

        while True:
            input_registered, key = self.input.wait_for_user_input()
            
            if input_registered:
                self.game.process_input(key)
                self.renderer.render(self.game.match)


if __name__ == "__main__":
    app = App()
    app.run()