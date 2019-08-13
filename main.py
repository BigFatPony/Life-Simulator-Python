import random

print("********* \n"
      "Welcome  Aggie's Life Simulator \n"
      "All these events are randomly generated \n"
      "********* \n")

class Player:

    def __init__(self,first,last,gender):
        self.first = first
        self.last = last
        self.gender = gender
first = input("Please enter first name: ")
last = input("Please enter last name: ")
gender = input("Please enter gender: ")


player1 = Player(first,last,gender)
print("You are named " + first + " " + last + ".") 



