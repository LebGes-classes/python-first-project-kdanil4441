import os


class Console:
    """Класс для работы с консолью и цветами."""

    RESET = "\033[0m"
    BLUE = "\033[44m"
    RED = "\033[91m"

    @staticmethod
    def clear() -> None:
        """
        Очищает консоль.
        """
        os.system("cls" if os.name == "nt" else "clear")