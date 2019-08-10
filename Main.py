import random
from random import randint

print("Welcome  Aggie's Life Simulator \n"
      "All these events are randomly generated \n"
      " \n")

class Player:
    gender = (randint(1,2))
    
if (Player.gender) == 1:
    print("You have been born a male")
    Player.gender = 1

else:
    print("You have been born a female")
    Player.gender = 2
