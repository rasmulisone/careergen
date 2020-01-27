import random
with open("clubs.txt") as file:
    clubs = file.readlines()
    careerclubs = random.randint(2, 9)
    for i in range(careerclubs):
        club = random.choice(clubs)
        print(club)
