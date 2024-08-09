import random
def game():
 player_choice = input("enter your choice:")
 computer_choice = ["rock","paper","scissor"]
 real_cc= random.choice(computer_choice)
 print("you choose" + player_choice + "computer choose" + real_cc)
 if(player_choice==real_cc):
    print("Its a tie!!")
 elif(player_choice=="rock" and real_cc=="paper"):
    print("You lost computer wins!!")
 elif(player_choice=="rock" and real_cc=="scissor"):
    print("You win!!")
 elif(player_choice=="paper" and real_cc=="rock"):
    print("You win!!")
 elif(player_choice=="paper" and real_cc=="scissor"):
    print("you lost computer wins")
 elif(player_choice=="scissor" and real_cc=="paper"):
    print("u wins computer lost")
 elif(player_choice=="scissor" and real_cc=="rock"):
    print("u lost computer wins")
def greeting():
    return "hii"
def position():
 response = greeting()
 positions = {1:"first", 2:"second", 3:"third"}
 print(response)

def factorial(n):
   if(n==0 or n==1):  return 1 
   else : return n*factorial(n-1)
def main():
    n = input(print("enter a number:"))
    print(factorial(n))

