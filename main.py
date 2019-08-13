import random

print("********* \n"
      "Welcome  Aggie's Life Simulator \n"
      "All these events are randomly generated \n"
      "********* \n")

class Player(object):

    def __init__(self,first,last,gender):
        self.first = first
        self.last = last
        self.gender = gender

first = input("Please enter first name: ")
last = input("Please enter last name: ")
gender = input("Please select a gender: \n"
                              "1. Male \n"
                              "2. Female \n")
while gender != "1" and gender != "2":
                    gender = input("Please select a gender: \n"
                                  "1. Male \n"
                                  "2. Female \n")

player1 = Player(first,last,gender)
print("You are named " + first + " " + last + ".")

def __init__(self,year):
        self.year = year
input("*Press Enter to age a year*")
print(" ")

def __init__(self,event):
        self.event = event
with open("Passive_Events.txt") as file:
                passive = random.choice(file.readlines())
print(passive)

