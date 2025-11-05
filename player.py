class Player:
    def __init__(
            self,
            health,
            heavy_attack,
            light_attack,
            defense,
            heavy_attack_pp,
            light_attack_pp,
            inventory
    ):
        self.health = health
        self.heavy_attack = heavy_attack
        self.light_attack = light_attack
        self.defense = defense
        self.heavy_attack_pp = heavy_attack_pp
        self.light_attack_pp = light_attack_pp
        self.inventory = inventory
