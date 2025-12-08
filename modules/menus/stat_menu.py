from modules.clear import clear
from modules.menus.selection_menu import selection_menu
import textwrap


def stat_menu(player):
    stat_names = ("Intelligence", "Charisma", "Deception", "Anger")
    menu_items = tuple(
        f"{name:<15} [{player.stats[i]}]" for i, name in enumerate(stat_names)
    ) + ("Reset",) + ("Continue",)
    while True:
        menu_text = textwrap.dedent(f"""
        Allocate stat points
        Available: {player.stat_points}
        """)
        selected = selection_menu(menu_items, menu_text)
        if selected == len(stat_names - 1):
            player.stats = [5, 5, 5, 5]
        elif selected == len(stat_names):
            ...
        else:
            if player.stat_points > 0:
                player.stats[selected] += 1
                player.stat_points -= 1
                print(f"You selected: {stat_names[selected]}")
            else:
                print("All stat points have been used")
        break
