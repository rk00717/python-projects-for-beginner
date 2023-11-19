from random import randrange

class GuessTheNumber:
    def user_guess(self, min_guess_limit, max_guess_limit):
        guess_count = 0
        guess = randrange(min_guess_limit, max_guess_limit)
        while(True):
            my_guess = int(input("::: "))
            guess_count +=1
            if(my_guess > guess):
                print("Sry. Your guess is too high to compare.")
            elif(my_guess == guess):
                print(f"Yea!! you{(' finally ' if guess_count >=2 else ' ')}guess the word.")
                break
            elif(my_guess < guess):
                print("Sry. Your guess is too low to compare.")
            else:
                pass

    def system_guess(self, min_guess_limit, max_guess_limit):
        guess_count = 0
        guess = randrange(min_guess_limit, max_guess_limit)
        while True:
            guess = randrange(min_guess_limit, max_guess_limit) if(min_guess_limit != max_guess_limit) else guess
            my_answer = input(f"Is {guess} is to High(H), to Low(L), or Correct(C) : ").lower()
            guess_count += 1
            if(my_answer == 'h'):
                guess -= 1
                # guess = guess - guess//2
                max_guess_limit = guess
            elif(my_answer == 'c'):
                print(f"Yeepy! I guessed the word correct in {guess_count} tries")
                break
            elif(my_answer == 'l'):
                guess += 1
                # guess = guess + guess//2
                min_guess_limit = guess
            else:
                pass

    def start_game(self):
        min_guess_limit = int(input("Minimum guess value : "))
        max_guess_limit = int(input("Maximum guess value : "))

        if(min_guess_limit>max_guess_limit):
            min_guess_limit, max_guess_limit = max_guess_limit, min_guess_limit
        
        preference = input("Who do you want to guess the number?\n System(S) or You(Y) : ").lower()
        if(preference == 'y'):
            self.user_guess(min_guess_limit, max_guess_limit)
        elif(preference == 's'):
            self.system_guess(min_guess_limit, max_guess_limit)
        else:
            self.start_game()