# CardTrick.py

import random

def main():
    # Declare variables
    column = 0
    loopCounter = 0

    # Declare the deck list
    deck = [0] * 52

    # Declare a 7 row by 3 column list
    play = [[0, 0, 0] for _ in range(7)]

    # Openning message
    print("Welcome.  I'm not the latest development in AI, but ")
    print("I'm a computer program that can performa card trick.")
    print("Let's begin!")
    print()
    print("Building the deck of cards...")

    # Call BuildDeck()
    BuildDeck(deck)

    print("Done! \n")
    seeDeck = input("Now would you like to see the deck (y/n)?")
    
    # Call PrintDeck()
    if seeDeck.lower() == "y":
            PrintDeck(deck)
        

    # Begin the main card trick loop
    for loopCounter in range(3):
        # Call Deal()
        Deal(deck, play)
        

        column = int(input("\nWhich column is your card in (0, 1, or 2)?: "))

        # Call PickUp()
        PickUp(deck, play, column)

    # Call SecretCard()
    SecretCard(deck)

    print("Thank you for playing the card trick!")


def PrintCard(card):
    rank = card % 13
    suit = card // 13

    # Rank
    if rank == 0:
        cardString = " Ace of "
    elif rank == 10:
        cardString = " Jack of "
    elif rank == 11:
        cardString = "Queen of "
    elif rank == 12:
        cardString = " King of "
    else:
        cardString = " " + str(rank + 1) + " of "

    # Suit
    if suit == 0:
        cardString += "Clubs    "
    elif suit == 1:
        cardString += "Diamonds "
    elif suit == 2:
        cardString += "Hearts   "
    else:
        cardString += "Spades   "

    print(cardString, end='')

def BuildDeck(deck):
    # Define local variables
    used = [0] * 52
    card = 0
    i = 0

    # Generate cards until the deck is full of integers
    while i < 52:
       # Generate a random integer between 0 and 51
       card = random.randint(0,51)
       

       # Test to see if the value has already been used
       if used[card] == 0:
           
           # If not, add it to the deck
            deck[i] = card
            used[card] = 1
            i += 1

        
    # End while loop
    return


def PrintDeck(deck):
    # Define local variables
    card = 0

    for card in range(52):
        PrintCard(deck[card])
        print()

    # End for loop
    print()


def Deal(deck, play):
    # Define local variables
    card = 0

    # Deal the cards from the deck to the play list
    print()
    print("   Column 0           Column 1           Column 2")
    print("=======================================================")

    for row in range(7):
        for col in range(3):
            play[row][col] = deck[card]
            card += 1


    # End nested for loop structure

    for row in range(7):
        PrintCard(play[row][0])
        PrintCard(play[row][1])
        PrintCard(play[row][2])
        print()
    


def PickUp(deck, play, column):
    # Define local variables
    card = 0
    row = 0

    # Identify the order of columns to pick up
    if column == 0:
        order = [1, 0, 2]
    elif column == 1:
        order = [0, 1, 2]
    else:
        order = [0, 2, 1]
    

    # Now pick up cards from the play list by column and put them in deck
    for col in order:
        for row in range(7):
            deck[card] = play[row][col]
            card += 1
    
    # End for loop structure
    return

def SecretCard(deck):
    # Define local variables
    card = 0

    print()
    print("Finding secret card...")
    for card in range(0, 10):
        PrintCard(deck[card])
        print()

    print("Your secret card is: ", end='')
    card += 1
    PrintCard(deck[card])
    print()
    

main()        

