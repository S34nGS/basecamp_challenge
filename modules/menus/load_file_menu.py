from modules.menus.selection_menu import selection_menu
import textwrap


def load_file_menu():
    a = None
    menu_items = (
        f"{a if a is not None else 'Empty'}",
        f"{a if a is not None else 'Empty'}",
        f"{a if a is not None else 'Empty'}",
        "Back"
    )

    while True:
        menu_text = textwrap.dedent(f"""
        Pick a save file
        """)
        selected = selection_menu(menu_items, menu_text)
        if selected == 0:
            if menu_items[selected] == 'Empty':
                return "empty"
            else:
                return "file1"
        elif selected == 1:
            if menu_items[selected] == 'Empty':
                return "empty"
            else:
                return "file2"
        elif selected == 2:
            if menu_items[selected] == 'Empty':
                return "empty"
            else:
                return "file3"
        elif menu_items[selected] == "Back":
            return "back"
