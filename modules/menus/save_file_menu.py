from modules.menus.selection_menu import selection_menu
from classes.saves import Saves
import textwrap


def save_file_menu():
    saves = Saves()
    file1 = saves.read_save_file("saves/file1.json")
    file2 = saves.read_save_file("saves/file2.json")
    file3 = saves.read_save_file("saves/file3.json")
    menu_items = (
        f"{'file1' if file1 is not None else 'Empty'}",
        f"{'file2' if file2 is not None else 'Empty'}",
        f"{'file3' if file3 is not None else 'Empty'}",
        "Back"
    )
    menu_text = textwrap.dedent("""
        Which file do you want to save to?
    """)
    while True:
        selected = selection_menu(menu_items, menu_text)
        if menu_items[selected] == 'Empty':
            saves.write_save_file(f"file{selected}.json")
        elif selected == 0 and menu_items[selected] != 'Empty':
            choice = saves.are_you_sure()
            if choice == "yes":
                saves.write_save_file(f"file{selected}.json")
            elif choice == "no":
                pass
        elif selected == 1 and menu_items[selected] != 'Empty':
            choice = saves.are_you_sure()
            if choice == "yes":
                saves.write_save_file(f"file{selected}.json")
            elif choice == "no":
                pass
        elif selected == 2 and menu_items[selected] != 'Empty':
            choice = saves.are_you_sure()
            if choice == "yes":
                saves.write_save_file(f"file{selected}.json")
            elif choice == "no":
                pass
        elif menu_items[selected] == "Back":
            return "back"
