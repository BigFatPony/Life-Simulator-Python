import random

print("********* \n"
      "Welcome  Aggie's Life Simulator \n"
      "All these events are randomly generated \n"
      "********* \n")

class Player:
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    
player = Player()
player.gender = random.randint(1,2)

if player.gender == Player.GENDER_MALE:
    print("You have been born a male.")
else:
    print("You have been born a female.")




