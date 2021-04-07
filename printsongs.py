# print_songs.py

def macdonald_verse(animal, sound):
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print("And on that farm he had a", animal + ", Ee-igh, Ee-igh, Oh!")
    print("With a", sound, sound, "here and a", sound, sound, "there.")
    print("Here a", sound + ", there a", sound + ", everywhere a", sound + ", "
          + sound + ".")
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")
    print()


def print_macdonald(animals, sounds):
    for i in range(len(animals)):
        macdonald_verse(animals[i], sounds[i])


def ants(number):
    print("The ants go marching", number, "by", number + ", hurrah! hurrah!")


def ants_verse(number, action):
    ants(number)
    ants(number)
    print("The ants go marching", number, "by", number + ",")
    print("The little one stops to", action + ",")
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! Boom! Boom!")
    print()


def print_ants():
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight",
               "nine", "ten"]
    actions = ["suck his thumb", "tie his shoe", "look at me",
               "settle the score", "plant a chive", "eat chex mix",
               "throw out some leaven", "see his mates", "check the time",
               "make a friend"]
    for i in range(10):
        ants_verse(numbers[i], actions[i])


def main():
    animals = [0, 0, 0, 0, 0]
    sounds = [0, 0, 0, 0, 0]
    for i in range(5):
        animals[i] = input("Enter an animal: ")
        sounds[i] = input("Enter this animal's sound: ")
    print()
    print_macdonald(animals, sounds)
    print()
    print_ants()


if __name__ == '__main__':
    main()
