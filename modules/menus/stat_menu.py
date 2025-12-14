from modules.menus.selection_menu import selection_menu
from classes.player import Player
import textwrap


def stat_menu(player: Player):
    menu_items = (
        f"Health        [{player.stats[0]}]",
        f"Strength      [{player.stats[1]}]",
        f"Intelligence  [{player.stats[2]}]",
        f"Charisma      [{player.stats[3]}]",
        f"Deception     [{player.stats[4]}]",
        f"Anger         [{player.stats[5]}]",
        "Reset",
        "Continue",
        "Back"
    )

    while True:
        menu_text = textwrap.dedent(f"""
        Allocate stat points
        Available: {player.stat_points}
        """)
        selected = selection_menu(menu_items, menu_text)
        if menu_items[selected] == "Reset":
            player.stats = [1, 1, 1, 1, 1, 1]
            player.stat_points = 6
        elif menu_items[selected] == "Continue":
            player.health = player.health + (5 * player.stats[0])
            player.max_health = player.max_health + (5 * player.stats[0])
            player.heavy_attack = player.heavy_attack + (1.5 * player.stats[1])
            player.light_attack = player.light_attack + (1.5 * player.stats[1])
            return "done"
        elif menu_items[selected] == "Back":
            return "back"
        else:
            if player.stat_points > 0:
                player.stats[selected] += 1
                player.stat_points -= 1
                print(f"You selected: {menu_items[selected]}")
            else:
                print("All stat points have been used")
        break
