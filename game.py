from maze import Maze
from player import Player
from renderer import Renderer
from menu import Menu
from console import Console


class Game:
    """Основной класс игры."""

    def __init__(self):
        """Инициализация игры."""
        self.level = 1
        self.menu = Menu()

    def run(self) -> None:
        """Запускает игру."""
        while True:
            choice = self.menu.show()

            if choice == "1":
                self.play()
            elif choice == "2":
                self.menu.show_rules()
            elif choice == "3":
                break

    def play(self) -> None:
        """Основной игровой цикл."""
        while True:
            maze = Maze(9 + self.level * 2)
            maze.generate()
            player = Player()

            while True:
                Renderer.draw(maze, player, self.level)
                key = input().lower()

                if key == "q":
                    return

                if key in ["w", "s", "a", "d"]:
                    self.move_player(key, player, maze)

                if (player.x, player.y) == maze.exit:
                    self.finish_level(player)
                    break

    def move_player(self, key: str, player: Player, maze: Maze) -> None:
        """
        Передвигает игрока.

        Args:
            key (str): Клавиша для передвижения.
            player (Player): Игрок.
            maze (Maze): Лабиринт.
        """
        moves = {
            "w": (0, -1),
            "s": (0, 1),
            "a": (-1, 0),
            "d": (1, 0),
        }

        dx, dy = moves[key]
        nx, ny = player.x + dx, player.y + dy

        if maze.is_free(nx, ny):
            player.x, player.y = nx, ny
            player.moves += 1

    def finish_level(self, player: Player) -> None:
        """
        Завершает уровень.

        Args:
            player (Player): Игрок.
        """
        Console.clear()
        print("Уровень пройден")
        print(f"Совершено ходов: {player.moves}")
        input("\nEnter - переход к следующему уровню")
        self.level += 1