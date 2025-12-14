from modules.menus.selection_menu import selection_menu
from modules.clear import clear
import textwrap


def menu():
    menu_items = (
        "Start",
        "Exit"
    )

    while True:
        menu_text = textwrap.dedent("""
            ----------------------------
                    PRISON ESCAPE
            ----------------------------
        """)
        selected = selection_menu(menu_items, menu_text)
        if menu_items[selected] == "Start":
            return "start"
        elif menu_items[selected] == "Exit":
            clear()
            print("You left the game")
            return "exit"
