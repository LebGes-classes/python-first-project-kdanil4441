from console import Console


class Menu:
    """Класс главного меню."""

    def show(self) -> str:
        """
        Отображает главное меню.

        Returns:
            str: Выбранный пункт меню.
        """
        Console.clear()
        print('\n')
        print("ЛАБИРИНТ\n")
        print("1. Начать игру")
        print("2. Правила")
        print("3. Выход\n")
        return input("Выберите пункт: ")

    def show_rules(self) -> None:
        """
         Выводит правила игры.
        """
        Console.clear()
        print('\n')
        print("ПРАВИЛА И УПРАВЛЕНИЕ\n")
        print("W — движение вверх")
        print("A — движение влево")
        print("S — движение вниз")
        print("D — движение вправо")
        print()
        print("Цель игры — дойти от символа @ до X (выход из лабиринта).")
        input("\nEnter — выход в меню")