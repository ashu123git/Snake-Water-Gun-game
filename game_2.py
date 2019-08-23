import random
from time import time
from pygame import *
mixer.init()
mixer.music.load("snake.ogg")
mixer.music.play(1)
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tWELCOME TO SNAKE, WATER, GUN. LET'S PLAY\n")
def game_2(a):
    lose_sound=mixer.Sound("lose.wav")
    win_sound=mixer.Sound("won.wav")
    loser_sound=mixer.Sound("loser.wav")
    lst=["snake","water","gun"]
    i=10
    comp_score=0
    your_score=0
    while i>0:
        mixer.music.unpause()
        a=input("\nIt's your turn : ")
        try:
            if a=="s":
                  print("You have choosen : ",a)
                  print("Now computer's turn : ")
                  b=random.choice(lst)
                  print("Computer's choice : ",b)
                  if b==lst[0]:
                      print("SAME MOVE.")
                      i-=1
                      print("Number of moves left with you = ",i)
                      print("Computer's score = ",comp_score,"\nYour score = ",your_score)
                      continue
                  elif b==lst[1]:
                      print("CONGRATS! YOU WON")
                      your_score+=1
                      i-=1
                      print("Number of moves left with you = ",i)
                      print("computer's score = ",comp_score,"\nYour score = ",your_score)
                      continue
                  elif b==lst[2]:
                      print("OOPS! COMPUTER WON")
                      mixer.Sound.play(lose_sound)
                      # time.sleep(2)
                      mixer.music.pause()
                      comp_score+=1
                      i-=1
                      print("Number of moves left with you = ",i)
                      print("Computer's score = ",comp_score,"\nYour score = ",your_score)
                      continue
            elif a=="w":
                     print("You have choosen : ",a)
                     print("Now computer's turn : ")
                     b = random.choice(lst)
                     print("Computer's choice : ", b)
                     if b == lst[0]:
                         print("OOPS! COMPUTER WON.")
                         mixer.Sound.play(lose_sound)
                         # time.sleep(2)
                         mixer.music.pause()
                         comp_score+=1
                         i-=1
                         print("Number of moves left with you = ",i)
                         print("Computer's score = ", comp_score, "\nYour score = ", your_score)
                         continue
                     elif b == lst[1]:
                           print("SAME MOVE!")
                           i-=1
                           print("Number of moves left with you = ",i)
                           print("computer's score = ", comp_score, "\nYour score = ", your_score)
                           continue
                     elif b == lst[2]:
                           print("CONGRATS! YOU WON")
                           your_score += 1
                           i-=1
                           print("Number of moves left with you = ",i)
                           print("Computer's score = ", comp_score, "\nYour score = ", your_score)
                           continue
            elif a=="g":
                     print("You have choosen : ",a)
                     print("Now computer's turn : ")
                     b = random.choice(lst)
                     print("Computer's choice : ", b)
                     if b == lst[0]:
                         print("CONGRATS! YOU WON.")
                         your_score += 1
                         i-=1
                         print("Number of moves left with you = ",i)
                         print("Computer's score = ", comp_score, "\nYour score = ", your_score)
                         continue
                     elif b == lst[1]:
                          print("OOPS! COMPUTER WON")
                          mixer.Sound.play(lose_sound)
                          # time.sleep(2)
                          mixer.music.pause()
                          comp_score+=1
                          i-=1
                          print("Number of moves left with you = ",i)
                          print("computer's score = ", comp_score, "\nYour score = ", your_score)
                          continue
                     elif b == lst[2]:
                          print("SAME MOVE!")
                          i-=1
                          print("Number of moves left with you = ",i)
                          print("Computer's score = ", comp_score, "\nYour score = ", your_score)
                          continue
            else:
                raise ValueError
        except ValueError:
            print("Enter correct choice : ")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tFINAL SCORES ARE AS FOLLOWS:-\n")
    print("Computer's score = ",comp_score,"\nYour score = ",your_score)
    if(your_score>comp_score):
        mixer.Sound.play(win_sound)
        time.sleep(4)
        print("\t\t\t\t\t\t\t\t\t\t\t\t\tCONGRATULATIONS! YOU HAVE WON THE GAME...")
        # mixer.Sound.play(win_sound)
        mixer.music.stop()
    elif(your_score<comp_score):
        mixer.Sound.play(loser_sound)
        print("\t\t\t\t\t\t\t\t\t\t\t\t\tBETTER LUCK NEXT TIME..")
        # time.sleep(4)
        # mixer.Sound.play(loser_sound)
        mixer.music.pause()

    else:
        print("Match Draw!")
        mixer.music.stop()
pass
choice=print("Enter your choice : \n--> Press s for snake\n--> Press w for water\n--> Press g for gun\n")
game_2(choice)
while mixer.music.get_busy():
    time.Clock().tick(10)