import os
import story
from battle import run_battle
import player
import enemy1
import enemy2

playing = False
battle = False
step = 0
enemy_step = 0

enemies = [enemy1, enemy2]

# Clear screen function
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()


# Main menu
while True:
    print("""
----------------------------
        PRISON ESCAPE  
----------------------------
        1. Start
        2. Info
        3. Exit
    """)
    choice = input("Type een nummer in: ")

    if choice == "1":
        clear()
        playing = True
        break
    elif choice == "2":
        clear()
        print("""
Het spel gaat over een persoon die vastzit in een gevangenis.
Het doel is om een aantal levels te voltooien en 
om vijanden die je tegenkomt in de gevangenis te verslaan. 
Waardoor je uitenedlijk kunt onstnappen 
        """)
    elif choice == "3":
        clear()
        print('Je hebt het spel verlaten.')
        break
    else:
        clear()
        print("Keuze is niet valide, probeer opnieuw.")


# Main game loop
while True:
    # Storyline loop
    if playing:
        print(story.storyline[step])
        a = input("a")
        if a == "y":
            clear()
            step += 1
            battle = True
            playing = False

    # Battle loop
    elif battle:
        run_battle(player, enemies[enemy_step])
        if run_battle(player, enemies[enemy_step]) == "Win":
            clear()
            print("You have beaten the enemy")
            enemy_step += 1
            playing = True
            battle = False
        elif run_battle(player, enemies[enemy_step]) == "Lose":
            clear()
            print("You died :(")
            break

    else:
        break
