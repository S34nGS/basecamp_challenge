light_attack = 5
light_attack_pp = 4
heavy_attack = 5
heavy_attack_pp = 5
defense = 3
inventory = [1, 2, 3, 4]

player_dict = {
    "1": [light_attack, light_attack_pp],
    "2": [heavy_attack, heavy_attack_pp],
    "3": defense
}

if len(inventory) == 4:
    player_dict["4"] = [inventory[0], inventory[0]]

print(player_dict.keys())