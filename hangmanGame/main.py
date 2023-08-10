import random
from hangmanArt import logo 
from hangmanArt import stages 
from hangmanWord import word_list

endOfGame = False
lives = 6

print(logo)

chosenWord = random.choice(word_list) 

guessWordsList = []

for letter in chosenWord:
    guessWordsList.append('_')  

while not endOfGame:
    
    guess = input("Enter a letter to guess the word : ").lower()
    if guess in guessWordsList:
        print("You have already Guessed this letter")
    else:
        for index  in range(len(chosenWord)):
            if chosenWord[index] == guess:
                guessWordsList[index] = guess
    
    if guess not in chosenWord:
        lives = lives-1
        if lives == 0:
            endOfGame = True
            print("you loose")
    
    print(f"{''.join(guessWordsList)}")
    
    if '_' not in guessWordsList:
        endOfGame = True
        print("You Won\n")        
        print(guessList)

    print(stages[lives])
