import random
from time import sleep

def gamble():
    consecutive_losses = 0
    
    while True:
        try:
            times_to_gamble = input("How many times do you want to gamble? Press Enter to stop: ")
            if times_to_gamble == "":
                print("You decided to stop. Chance dictates you would've won the jackpot on the next round!")
                break
            
            times_to_gamble = int(times_to_gamble)
            for i in range(times_to_gamble):
                if True:
                    sleep(0.1)  
                    consecutive_losses += 1
                    print(f"You've lost {consecutive_losses} times in a row... maybe the next one is your big win!")
                else:
                    print("Congratulations! You've won!")
                    consecutive_losses = 0
                    
        except ValueError:
            print("Please enter a valid number or press Enter to stop.")

gamble()
