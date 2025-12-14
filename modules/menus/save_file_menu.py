from modules.menus.selection_menu import selection_menu
from classes.saves import Saves
from classes.player import Player
from classes.weapon import Weapon
import textwrap


def save_file_menu(player: Player, story_step: int, enemy_step: int):
    current_save = {
        "health": player.health,
        "max_health": player.max_health,
        "stats": player.stats,
        "stat_points": player.stat_points,
        "name": player.name,
        # "weapon_name": weapon.name,
        # "weapon_durability": weapon.durability,
        "heavy_attack_pp": player.heavy_attack_pp,
        "light_attack_pp": player.light_attack_pp,
        "story_step": story_step,
        "enemy_step": enemy_step
    }
    saves = Saves()
    file1 = saves.read_save_file("saves/file1.json")
    file2 = saves.read_save_file("saves/file2.json")
    file3 = saves.read_save_file("saves/file3.json")
    menu_items = (
        f"{file1['name'] if file1 is not None else 'Empty'}",
        f"{file2['name'] if file2 is not None else 'Empty'}",
        f"{file3['name'] if file3 is not None else 'Empty'}",
        "Back"
    )
    menu_text = textwrap.dedent("""
        Which file do you want to save to?
    """)
    while True:
        selected = selection_menu(menu_items, menu_text)
        if menu_items[selected] == 'Empty':
            saves.write_save_file(f"saves/file{selected + 1}.json", current_save)
            return "saved"
        elif selected == 0 and menu_items[selected] != 'Empty':
            choice = saves.are_you_sure()
            if choice == "yes":
                saves.write_save_file(f"saves/file{selected + 1}.json", current_save)
                return "saved"
            elif choice == "no":
                pass
        elif selected == 1 and menu_items[selected] != 'Empty':
            choice = saves.are_you_sure()
            if choice == "yes":
                saves.write_save_file(f"saves/file{selected + 1}.json", current_save)
                return "saved"
            elif choice == "no":
                pass
        elif selected == 2 and menu_items[selected] != 'Empty':
            choice = saves.are_you_sure()
            if choice == "yes":
                saves.write_save_file(f"saves/file{selected + 1}.json", current_save)
                return "saved"
            elif choice == "no":
                pass
        elif menu_items[selected] == "Back":
            return "back"
