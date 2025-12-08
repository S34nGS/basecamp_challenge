from readchar import key, readkey
from modules.clear import clear
from typing import Optional


def selection_menu(menu: tuple[str], text_to_print: Optional[str] = None) -> int:
    selected = 0
    while True:
        clear()
        if text_to_print is not None:
            print(text_to_print)
        longest = len(max(menu, key=len))

        print(f"╔{'═' * (longest + 4)}╗")

        for index in range(len(menu)):
            if index == selected:
                print(f"║> {menu[index]} {' ' * (longest - len(menu[index]))}<║")
            else:
                print(f"║  {menu[index]} {' ' * (longest - len(menu[index]))} ║")

        print(f"╚{'═' * (longest + 4)}╝")
        pressed = readkey()

        if pressed == key.DOWN and selected < len(menu) - 1:
            selected += 1
        elif pressed == key.UP and selected > 0:
            selected -= 1
        elif pressed == key.ENTER:
            return selected
