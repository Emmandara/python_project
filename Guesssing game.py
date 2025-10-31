# guess_the_number.py

# function for setting difficulty
import random
DIFFICULTIES = {
        #this dictionary will store the components that makes the game  atch its difficulty 
        "easy":            {"low": 1, "high": 20,  "max_attempts": 6,  "hint_mode": "full",    "hint_limit": None},
        "medium":          {"low": 1, "high": 50,  "max_attempts": 8,  "hint_mode": "full",    "hint_limit": None},
        "hard":            {"low": 1, "high": 100, "max_attempts": 8, "hint_mode": "full", "hint_limit": None},
        "extremely hard":  {"low": 1, "high": 150, "max_attempts": 8,  "hint_mode": "limited",    "hint_limit": 5},
        "impossible":      {"low": 1, "high": 1000, "max_attempts": 5,  "hint_mode": "limited", "hint_limit": 2},  
    }
def difficulties():
  # this function is used for chosssing difficulty

    print(" Guess the Number Game")
    print("Choose difficulty: Easy / Medium / Hard / Extremely Hard / Impossible")

    while True:
        choice = input("> ").strip().lower()
        if choice in DIFFICULTIES:
            return choice, DIFFICULTIES[choice].copy()
        print("Please enter a valid difficulty!")
def init_game_state(settings):
    #this function will initialize the stats at beginning, it takes in settings which will have difficiulty choice
    return {
        "low":         int(settings["low"]),
        "high":        int(settings["high"]),
        "max_attempts":settings["max_attempts"],
        "hint_mode":   settings["hint_mode"],
        "hints_left":  settings["hint_limit"],  
        "secret":      random.randint(int(settings["low"]), int(settings["high"])),
        "attempts":    0,
        "score":       100,
        "hints_used":  0
    }

def main_game(settings):
    info = init_game_state(settings)
    low,high =info["low"], info["high"]
    hint_mode = info["hint_mode"]
    hints_left = info["hints_left"]

    print("Im thinking of  a number between",low," and", high)
    print("You have a max number attempts of ",info['max_attempts'])
    if info["hint_mode"] == "limited":
        print("  Hints are LIMITED: you have" ,info['hints_left'] ,"total high/low hints.")
    while info["attempts"] < info["max_attempts"]:
        guess = input ("Please enteer your guess ")
        if not guess.isdigit():
            print(" Please enter a valid whole number.")
            continue
        guess = int(guess)
        if not (low <= guess <= high):
            print("Stay within range ",low ,high)
            continue
        info["attempts"] += 1
        if guess == info["secret"]:
            print(" Correct! You guessed it in", info["attempts"], " tries.")
            return True
            
        # logic for hints
        if hint_mode == "full":
            if guess < info["secret"]:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        elif  hint_mode == "limited":
            if hints_left and hints_left > 0:
                if guess < info["secret"]:
                    print("Too low! Try again.")
                else:
                    print("Too high! Try again.")
                hints_left -= 1
                print("(Hints left: ",hints_left,")")
            else:
                print("Wrong! No hints left.")

        else:  
            print("Incorrect! Try again.")

        if info["attempts"] == info["max_attempts"]:
            print(" Game Over! The number was ",info['secret'],".")
            return False    
def choose_mode():
    while True:
        try:
            answer = input("Chosse which mode you would like to play 'Single game' or 'Survival mode'").strip().lower()
            if answer in ("single" ):
                return "single" ,1
            elif answer in ("survival" , "survival mode"):
                return "Survival", 3
            else:
                raise ValueError("Invalid mode")
        except ValueError:
             print("PLease type 'Single' or 'Survival'")
        # --- main section ---
print("===================================")
print("      WELCOME TO GUESS THE NUMBER ")
print("===================================")
print("Test your luck and logic!")
#this allows to play again whilst error handling
count=0


while True:
        try:
            ready = input("Are you ready to play? (yes/no): ").strip().lower()
            
               
            if ready == "yes":
                        choice, settings = difficulties()
                        print("You chose:",choice.title())
                        order = list(DIFFICULTIES.keys())
                        
                        current= order.index(choice) 
                        mode_name  , lives = choose_mode()
                        print("Mode name ",mode_name," lives",lives)
                        while lives >0:  
                            
                            
                            if main_game(settings):
                                print("You won this round") 
                                count += 1
                                if mode_name == "single":
                                     break
                            
                                    
                                if count >= 3:
                                    if current < len(order)-1:
                                        next= order[current +1]
                                        choice = next
                                        settings = DIFFICULTIES[choice]
                                        print("Difficuty has increased to",choice.title(),"!")
                                    
                                    else:
                                        print("You are the highest level keep going ")
                            else:
                                lives -= 1
                                if lives> 0:
                                    print(" Round lost. Lives remaining: ",lives,". Starting next round...")
                                    continue
                                else:
                                    print(" No lives left. Better luck next time")
                                    break
                                         


                                      
                                      
                                 
                                 
                               
                        while True:
                                    try:
                                        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
                                        if play_again in ("yes"):
                                            print("Restarting game...")
                                            break  
                                        elif play_again in ("no"):
                                            print("Thanks for playing! ")
                                            quit()
                                        else:
                                            raise ValueError("Invalid response")
                                    except ValueError:
                                        print(" Please type 'yes' or 'no'.")
                        continue 

            elif ready == "no":
                    print("Maybe next time! ")
                    quit()
            else:
                    raise ValueError("Invalid response")
        except ValueError:
            print(" Please type 'yes' or 'no'.")
        except (KeyboardInterrupt, EOFError):
            print("OOOps there seems to be an inturoption Exiting game...  Thanks for playing!")
            quit()