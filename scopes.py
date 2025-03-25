#########################scopes###########################
# enemies = 1
# def increase_enemies():
#     print(f"enemies inside function {enemies}")

# increase_enemies()
# print(f"enemies outside function {enemies}")

 #Local scope

# def drink_potion():
#      potion_strength = 2
#      print(potion_strength)
# drink_potion()

#Global scope
# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)
# drink_potion()

# There is no block scope
# game_level = 3
# enemies = ["skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy =enemies[2]
#     print(new_enemy)

#Modifying Global scope
enemies = 1
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

increase_enemies()
print(f"enemies inside function:{enemies}")

#Global constants
PI = 3.14


