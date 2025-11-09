import random


class Player:
    def __init__(
            self,
            health: int,
            heavy_attack: int,
            light_attack: int,
            defense: int,
            heavy_attack_pp: int,
            light_attack_pp: int,
            inventory: list
    ):
        self.health = health
        self.heavy_attack = heavy_attack
        self.light_attack = light_attack
        self.defense = defense
        self.heavy_attack_pp = heavy_attack_pp
        self.light_attack_pp = light_attack_pp
        self.inventory = inventory

    def attack(self, enemy, enemy_choice, attack_type):
        if attack_type == "light" and self.light_attack_pp > 0:
            self.light_attack_pp -= 1
            if enemy_choice != "3":
                enemy.health -= self.light_attack
            else:
                if self.light_attack > enemy.defense:
                    enemy.health -= (self.light_attack - enemy.defense)
                else:
                    print("The defense of the enemy is too strong")
        elif attack_type == "heavy" and self.heavy_attack_pp > 0:
            self.heavy_attack_pp -= 1
            if enemy_choice != "3":
                enemy.health -= self.heavy_attack
            else:
                if self.heavy_attack > enemy.defense:
                    enemy.health -= (self.heavy_attack - enemy.defense)
                else:
                    print("The defense of the enemy is too strong")
        else:
            print("You can't do that attack anymore")

    def weapon(self, enemy, enemy_choice, inventory_slot):
        weapon = self.inventory[inventory_slot]
        if weapon.durability <= 0:
            print("You can't do that attack anymore")
            return

        if weapon.name == "Shuriken":
            randomized_number = random.randint(1, 3)
            damage = weapon.damage * randomized_number
            weapon.durability -= randomized_number
            print(f"You threw {randomized_number} shuriken(s)!")
        else:
            damage = weapon.damage
            weapon.durability -= 1

        if enemy_choice != "3":
            enemy.health -= damage
        else:
            if damage > enemy.defense:
                enemy.health -= (damage - enemy.defense)
            else:
                print("The defense of the enemy is too strong")

    def defend(self, enemy, enemy_choice):
        if enemy_choice != "3" and (self.defense > enemy.light_attack or self.defense > enemy.heavy_attack):
            print("You defended against the enemy")
        elif enemy_choice != "1" and self.defense < enemy.light_attack:
            self.health -= enemy.light_attack
        elif enemy_choice != "2" and self.defense < enemy.heavy_attack:
            self.health -= enemy.heavy_attack
