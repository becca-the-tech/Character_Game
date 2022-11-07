import time
import random


def print_pause(input):
    print(input)
    time.sleep(2)


def intro(enemy):
    descriptions = ["forested", "barren", "snowy", "water-y",
                    "hostile", "flowery"]
    noises = ["roar", "cackle", "shriek", "snort", "yelp", "scary whisper"]

    descriptive = random.choice(descriptions)
    noise = random.choice(noises)

    print_pause(f"You awaken in a {descriptive} landscape.")
    print_pause("Upon looking around, you see everyone cowering.")
    print_pause(f"They explain they are hiding from {enemy}.")
    print_pause(f"In the distance, you hear a {noise}..")
    print_pause("the sound of thundering steps comes closer.\n")


def choose_attack_or_flee():
    while True:
        print_pause("Would you like to attack or flee?")
        choice = input("Type '1' for attack, '2' for flee.\n")
        if choice == "1":
            break
        elif choice == "2":
            break
        else:
            print("Invalid input.")
    return choice


def attack_or_flee(enemy, enemy_hit_points):
    if choose_attack_or_flee() == "1":
        braveryMultiplier = random.randint(1, 5)
        attack(braveryMultiplier, enemy, enemy_hit_points)
    else:
        flee(enemy, enemy_hit_points)


def attack(braveryMultiplier, enemy, enemy_hit_points):
    damage = random.randint(5, 10) * braveryMultiplier
    chance_of_loss = random.randint(1, 10) - braveryMultiplier

    if chance_of_loss >= 7:
        lose(enemy)
    else:
        print_pause(f"\n{enemy} has {enemy_hit_points} hit points")
        print_pause("You attack with all your might.")
        print_pause(f"You deal {damage} points of damage to {enemy}.")
        if enemy_hit_points <= damage:
            print_pause("\nTa da! Your bravery paid off!")
            print_pause(f"You defeated {enemy}!")
            win(enemy)
        else:
            enemy_hit_points = enemy_hit_points - damage
            print_pause(f"{enemy} only has {enemy_hit_points} left now.\n")
            attack_or_flee(enemy, enemy_hit_points)


def flee(enemy, enemy_hit_points):
    print_pause("You join the cowering villagers.")
    print_pause(f"But it does no use, {enemy} eventually finds you.")
    print_pause("Due to your fear, you must attack and hope for the best.")
    attack(1, enemy, enemy_hit_points)


def win(enemy):
    print_pause("\nThe villagers erupt into applause.")
    print_pause(f"{enemy} apologizes for their mean ways.")
    print_pause("And promises to make up for their actions with kind deeds.")
    print_pause("YOU WON!\n")
    play_again()


def lose(enemy):
    print_pause(f"\n{enemy} strikes you down with their powers.")
    print_pause("They cackle with glee. No one stands in their way now.")
    print_pause("They can now take over the world...")
    print_pause("starting with stealing all left socks!")
    print_pause("GAME OVER!\n")
    play_again()


def play_again():
    while True:
        choice = input("Would you like to play again? 'y' or 'n'\n").lower()
        if choice == 'y':
            play_game()
            break
        elif choice == 'n':
            print_pause("Thank you for playing!")
            print_pause("Have a great day!")
            break
        else:
            print("Invalid input.")


def play_game():
    enemies = ["Tigo the Intimidating Giraffe",
               "Yaxi the Fire-Breathing Lizard",
               "Mensi the Giant Snail", "Zaza the Venomous Leopard"]
    enemy = random.choice(enemies)
    enemy_hit_points = random.randint(10, 50)
    intro(enemy)
    attack_or_flee(enemy, enemy_hit_points)


play_game()
