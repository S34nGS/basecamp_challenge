import json
from modules.menus.selection_menu import selection_menu


class Saves:
    def __init__(self):
        pass

    def read_save_file(self, file: str) -> dict:
        try:
            with open(file, "r") as f:
                data = json.load(f)
                return data
        except FileNotFoundError:
            return None

    def write_save_file(self, file: str, save_data: dict):
        save_file = json.dumps(save_data, indent=4)
        with open(file, "w") as f:
            f.write(save_file)
            return "done"

    def want_to_save(self):
        menu_items = ("Yes", "No")
        menu_text = "Do you want to save?"
        while True:
            selected = selection_menu(menu_items, menu_text)
            if menu_items[selected] == "Yes":
                return "yes"
            elif menu_items[selected] == "No":
                return "no"

    def are_you_sure(self):
        menu_items = ("Yes", "No")
        menu_text = "Are you sure you want to overwrite this file?"
        while True:
            selected = selection_menu(menu_items, menu_text)
            if menu_items[selected] == "Yes":
                return "yes"
            elif menu_items[selected] == "No":
                return "no"

    def back_to_checkpoint(self):
        menu_items = ("Checkpoint", "Exit")
        menu_text = "You died :(\nDo you want to go back to a checkpoint or exit the game?"
        while True:
            selected = selection_menu(menu_items, menu_text)
            if menu_items[selected] == "Checkpoint":
                return "checkpoint"
            elif menu_items[selected] == "Exit":
                return "exit"
