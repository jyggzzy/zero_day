import random


def guess(x):
    random_number = random.randint(5, x)
    guess = 5
    try:
        while guess != random_number:
            guess = int(input(f"Guess Man Utd's position at end of season 💀: "))
            if guess > random_number:
                print("Give yourself some credit; you're not that poor 😊")
            elif guess < random_number:
                print("haq haq haq haq haq. Be realistic bro 🌚")

        print(f"You even sabi say na {random_number}'th be the best wey you go fit carry las las 😂😋💀")
    except ValueError:
        pass


guess(10)
