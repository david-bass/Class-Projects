
high = 100
low = 0
guessed = False
print('Please think of a number between 0 and 100!')

while not guessed:
    guess = (high + low)//2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if user_inp == 'c':
        guessed = True
    elif user_inp == 'h':
        high = guess
    elif user_inp == 'l':
        low = guess
    else:
        print("Sorry, I did not understand your input.")
        
print('Game over, your number is:' + str(guess))



print('Exercise: guess my number')

hi = 100
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)//2
    print("Is your secret number " + str(guess)+ "?")
    user_inp = input("Enter 'h' to indicate the number is too high. Enter 'l' to indicate the number is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess
    else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(guess))

