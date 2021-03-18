import time
import random
animals = ["lion", "tiger", "Leopard"]


def print_pause(msg):
    print(msg)
    time.sleep(2)


def err():
    print_pause("Please Write a valid number\n")


def end():
    print("Good bye")


def retry():
    last = input("Do you need to retry??!" + "1.Yes or 2.no\n")
    if last == "1":
        story()
    elif last == "2":
        end()
    else:
        err()
        retry()


def animalfield():
    print_pause("The steps was for a " + random.choice(animals) +
                ",he caught you and now it is eating you")
    print("You had lost The Game")
    retry()


def light():
    print_pause("While going to the light you heard steps behind you\n")
    choice = input("1.You will continue walking\n"
                   "2.You will stop\n"
                   "3.run fast and hide\n")
    if choice == "1":
        animalfield()
    elif choice == "2":
        animalfield()
    elif choice == "3":
        animalfield()
    else:
        err()
        light()


def cave():
    print_pause("you have 2 choices\n")
    choice = input("1.get into the deep of the cave\n"
                   "2.sleep near to the door and wait for the next day\n")
    if choice == "2":
        print_pause("A " + random.choice(animals) +
                    " came and ate you while sleeping\n")
        print("You had Lost the Game")
        retry()
    elif choice == "1":
        print_pause("You found some one and he rescued you\n")
        print("Congratulation! You won The game")
        retry()
    else:
        err()
        cave()


def story():
    print("You are in the desert"
          "it's so dark there is a storm in the desert"
          ",there is a small light so far from you"
          "there is a small cave near to you\n")
    choice = input("1.go to the light\n2.get into the cave\n")
    if choice == "1":
        light()
    elif choice == "2":
        cave()
    else:
        err()
        story()


story()
