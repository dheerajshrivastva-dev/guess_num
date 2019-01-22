import random
winning_num = random.randint(1,100)

print("hello play the game GUESS A NUM BETWEEN 1 TO 100: ")
print("lucky if you WIN in first time.")
guess_num = int(input("hey guess number : "))

guesses = 1

game_over = False
while not game_over:
     if guess_num == winning_num :
         print(f"YOU WON in {guesses} times")
         game_over = True

     else :

         if guess_num < winning_num:

             print("too low ! ")
             
         else:
             print("too high ! ")
         guesses += 1
         guess_num = int(input("hey guess number again : "))

if( winning_num == guess_num) and guesses <3:
    print("so impresive")
elif ( winning_num == guess_num) and guesses <4:
    print("good !")
elif ( winning_num == guess_num) and guesses <5:
    print("not bad !")
elif ( winning_num == guess_num) and guesses <6:
    print("it is OK !")
elif ( winning_num == guess_num) and guesses >6:
    print("try your best !")