#has to have a random function to get the value genereted between 100

#compare function to get in an input by user and use that value and guessed number to output an result
import random

print("Welcome to the guessing game!")

g = random.choice(range(100))

def hardness():
  '''asks hardness level and returns n value'''
  level = input("set hardness: easy or hard : ")
  if level == "easy":
    return 10
  elif level == "hard":
    return 5
  else:
    print("enter easy or hard")
    hardness()

hardness = hardness()

def ask_input():
  user_input = int(input("enter a number between 1 to 100 : "))
  return user_input


def main_loop():
  correct = False
  n = 0
  while not correct: 
    u = ask_input()
    if u==g:
      print("correct guess")
      correct = True
      break
    elif u>g:
      print("too high")
    elif u<g:
      print("too low")
    n+=1
    print(f"you got {hardness-n} guesses left to go")
    if n==hardness:
      print("ran out of choices")
      break
    
    
main_loop()