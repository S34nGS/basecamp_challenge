from modules.menus.selection_menu import selection_menu
import textwrap


def new_or_load_menu():
    menu_items = ("New Game", "Load Game", "Go Back")
    while True:
        menu_text = textwrap.dedent("""
            ----------------------------
                    PRISON ESCAPE
            ----------------------------
        """)
        selected = selection_menu(menu_items, menu_text)
        if menu_items[selected] == "New Game":
            return "new"
        elif menu_items[selected] == "Load Game":
            # TODO Use save files for this
            return "load"
        elif menu_items[selected] == "Go Back":
            return "back"
