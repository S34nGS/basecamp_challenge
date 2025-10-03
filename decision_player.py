health=100

heavy_attack=25
light_attack=10

enemy_health=100

inventory=["rock", "pepperspray", "knife", "shuriken"]



print("your inventory:", inventory)

print(f"your health:{health}, enemy_health:{enemy_health}")
while enemy_health>0:
  print("defeat the enemy ")
  option=input("Choose an item: ")

  if option.lower()=="rock":
    print("you lightly injury the fellow prisoner with a rock")
    enemy_health-=light_attack
    enemy_health=max(0,enemy_health)
  elif option.lower()=="pepperspray":
    print("you lightly injury the fellow prisoner with a rock")
    enemy_health-=light_attack
    enemy_health=max(0,enemy_health)
  elif option.lower()=="knife":
    print("you heavily injury the fellow prisoner with a knife")
    enemy_health-=heavy_attack
    enemy_health=max(0,enemy_health)
  elif option.lower()=="shuriken":
    print("you heavily injury the fellow prisoner with a shuriken")
    enemy_health-=heavy_attack
    enemy_health=max(0,enemy_health)
     
  else:
   print("not valid")

  print(f"jouw_health:{enemy_health}")

