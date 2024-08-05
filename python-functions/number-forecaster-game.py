import random

random_number = random.randint(1, 100)
player_lifePoints = 0

while True:
    player_lifePoints = int(
        input(
            "\nChoose how many attempts you need to find a number that is in my microchips\nThe number should be between 1-10:"))
    if player_lifePoints > 10 or player_lifePoints < 1:
        print("Incorrect value!")
    else:
        break

playerHasLives = player_lifePoints != 0
count = 0
while playerHasLives:
    player_lifePoints -= 1
    count += 1
    player_number = int(
        input("\nPlease enter a number between 1-100 and see if it's the same number I was thinking of... :D\t"))

    if random_number == player_number:
        print(f"\nCongratulations! You found what I chose at {count} step! Your points are {100 - ((count - 1) * 10)}")
        break
    elif player_number > random_number and playerHasLives:
        print("Think wisely.. (Maybe you should try lower numbers:)")
    elif player_number < random_number and playerHasLives:
        print("Think wisely.. (Maybe you should try higher numbers:)")

    print(f"You have {player_lifePoints} lives!")

    if player_lifePoints == 0:
        print(f"You are out of lives! The number was {random_number}")
        break
