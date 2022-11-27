import random

def deal_cards():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

def compute_scores(cards):
  if sum(cards)==21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1) 
  return sum(cards)


def compare_score(user_score,computer_score):
  if user_score > 21 and computer_score > 21:
    print("you lose went over 21")
  elif user_score == computer_score :
    print("it's a draw") 
  elif computer_score ==0:
    print("you lose oppenent has black jack")
  elif user_score == 0 :  
    print("won with a blackjack")
  elif user_score>21:
    print("you lose went over 21")
  elif computer_score > 21: 
    print("you won oppenent went over")   
  elif user_score > computer_score : 
    print("you won by high score")
  else:
    print("you lose by lower score than computer")


def playgame():
  user_cards=[]
  computer_cards=[]
  gameover=False
  
  for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
  while not gameover:
   computer_score=compute_scores(computer_cards)
   user_score = compute_scores(user_cards)
   print(f"you have {user_cards} with score: {user_score}")
   print(f"computer has {computer_cards[0]}")
   if computer_score==0 or user_score==0 or user_score> 21 :
      gameover=True
   else:
     if input("do you want to add a card? : enter y for yes and n for no: ") =="y":
        user_cards.append(deal_cards())
     else:
        gameover = True

  while  computer_score !=0 and computer_score<17:
   computer_cards.append(deal_cards())
   computer_score=compute_scores(computer_cards)

  print(f"your final hand is {user_cards}: score is {user_score}")
  print(f"computer has {computer_cards}: score is {computer_score}")
  compare_score(user_score,computer_score)


while input("do you want to play a game of blackjack?: y for yes n for no : ") =="y":
  playgame()




    

