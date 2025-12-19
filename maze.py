import random


class Maze:
    """Класс, отвечающий за логику лабиринта."""

    WALL = 1
    PATH = 0

    def __init__(self, size: int):
        """
        Инициализация лабиринта.

        Args:
            size (int): Размер лабиринта.
        """
        self.size = min(size, 25)
        if self.size % 2 == 0:
            self.size += 1
        self.grid = [[Maze.WALL] * self.size for i in range(self.size)]
        self.start = (1, 1)
        self.exit = None

    def generate(self) -> None:
        """
        Генерирует лабиринт.
        """
        self._create()
        self._find_farthest_exit()

    def _create(self) -> None:
        """Создает лабиринт."""
        stack = [self.start]

        while stack:
            x, y = stack[-1]
            self.grid[y][x] = Maze.PATH

            directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
            random.shuffle(directions)

            found = False
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 1 <= nx < self.size - 1 and 1 <= ny < self.size - 1:
                    if self.grid[ny][nx] == Maze.WALL:
                        self.grid[y + dy // 2][x + dx // 2] = Maze.PATH
                        stack.append((nx, ny))
                        found = True
                        break

            if not found:
                stack.pop()

    def _find_farthest_exit(self) -> None:
        """
        Находит самую дальнюю точку от старта для выхода.
        """
        visited = [[False] * self.size for i in range(self.size)]
        queue = [(self.start[0], self.start[1], 0)]
        visited[self.start[1]][self.start[0]] = True

        farthest_point = self.start
        max_distance = 0

        while queue:
            x, y, dist = queue.pop(0)

            if dist > max_distance:
                max_distance = dist
                farthest_point = (x, y)

            neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy

                if 1 <= nx < self.size - 1 and 1 <= ny < self.size - 1:
                    if self.grid[ny][nx] == Maze.PATH and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((nx, ny, dist + 1))

        self.exit = farthest_point

    def is_free(self, x: int, y: int) -> bool:
        """
        Проверяет, является ли клетка проходимой.

        Args:
            x (int): Координата X.
            y (int): Координата Y.

        Returns:
            bool: True если клетка свободна, иначе False.
        """
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.grid[y][x] == Maze.PATH
        return False