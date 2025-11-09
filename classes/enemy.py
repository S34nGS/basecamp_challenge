class Enemy:
    def __init__(self, health: int, heavy_attack: int, light_attack: int, defense: int):
        self.health = health
        self.heavy_attack = heavy_attack
        self.light_attack = light_attack
        self.defense = defense

    def attack(self, player, player_choice, enemy_choice):
        if enemy_choice == "1":
            attack_sort = self.light_attack
        elif enemy_choice == "2":
            attack_sort = self.heavy_attack
        elif enemy_choice == "3":
            attack_sort = self.defense

        if player_choice != "3" and enemy_choice in ("1", "2"):
            player.health -= attack_sort
        elif player_choice == "3" and enemy_choice in ("1", "2"):
            player.health -= (attack_sort - player.defense)
