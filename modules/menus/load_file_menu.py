from modules.menus.selection_menu import selection_menu
from classes.saves import Saves
from classes.player import Player
import textwrap


def load_file_menu(player: Player):
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
        Pick a save file
    """)
    while True:
        selected = selection_menu(menu_items, menu_text)
        if menu_items[selected] == 'Empty':
            menu_text = "\nThat save file is empty\n"
        elif selected == 0 and menu_items[selected] != 'Empty':
            player.health = file1["health"]
            player.max_health = file1["max_health"]
            player.stats = file1["stats"]
            player.stat_points = file1["stat_points"]
            player.name = file1["name"]

            # file1["weapon_name"].durability = file1["weapon_durability"]
            # player.inventory.append(file1["weapon_name"])
            # file1["weapon_name"].durability = file1["weapon_durability"] if file1["weapon_name"].durability else None
            # player.inventory.append(file1["weapon_name"]) if file1["weapon_name"] else None

            player.heavy_attack_pp = file1["heavy_attack_pp"]
            player.light_attack_pp = file1["light_attack_pp"]
            return "file1", file1
        elif selected == 1 and menu_items[selected] != 'Empty':
            player.health = file2["health"]
            player.max_health = file2["max_health"]
            player.stats = file2["stats"]
            player.stat_points = file2["stat_points"]
            player.name = file2["name"]
            # file2["weapon_name"].durability = file2["weapon_durability"]
            # player.inventory.append(file2["weapon_name"])
            player.heavy_attack_pp = file2["heavy_attack_pp"]
            player.light_attack_pp = file2["light_attack_pp"]
            return "file2", file2
        elif selected == 2 and menu_items[selected] != 'Empty':
            player.health = file3["health"]
            player.max_health = file3["max_health"]
            player.stats = file3["stats"]
            player.stat_points = file3["stat_points"]
            player.name = file3["name"]
            # file3["weapon_name"].durability = file3["weapon_durability"]
            # player.inventory.append(file3["weapon_name"])
            player.heavy_attack_pp = file3["heavy_attack_pp"]
            player.light_attack_pp = file3["light_attack_pp"]
            return "file3", file3
        elif menu_items[selected] == "Back":
            return "back"
