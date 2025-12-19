from console import Console


class Renderer:
    """Класс, отвечающий за отрисовку лабиринта."""

    CELL = "  "

    @staticmethod
    def draw(maze, player, level) -> None:
        """
        Отрисовка лабиринт.

        Args:
            maze: Лабиринт.
            player: Пользователь.
            level (int): Текущий уровень.
        """
        Console.clear()
        print('\n')

        for y in range(maze.size):
            for x in range(maze.size):
                if (x, y) == (player.x, player.y):
                    print(Console.RED + "@ " + Console.RESET, end="")
                elif (x, y) == maze.exit:
                    print(Console.RED + "X " + Console.RESET, end="")
                elif maze.grid[y][x] == maze.WALL:
                    print(Console.BLUE + Renderer.CELL + Console.RESET, end="")
                else:
                    print(Renderer.CELL, end="")
            print()

        print(f"\nУровень: {level}")
        print(f"Ходов совершено: {player.moves}")
        print("Для управления используйте клавиши W A S D")
        print("Q — выход в меню")