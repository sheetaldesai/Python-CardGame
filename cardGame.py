from random import shuffle

# class Deck represents the deck of cards
class Deck(object) :
    def __init__(self, picture) :
        self.picture = picture # unique identifier
        self.totalCards = 52
        self.deckList = [] # list of cards 

    # This method builds the deck 
    def createDeckList(self) :
        # i represents the suit
        for i in range(0,4) :
            # j represents the number
            for j in range(1,14) :
                # create a Card object of suit i and num j and add it my deckList
                card = Card(i,j)
                self.deckList.append(card)
        return self
    
    # This method shuffles the deck. It assumes that the deck is already created.
    def shuffle(self) :
        shuffle(self.deckList)
        return self

    # This method prints the deckList
    def printDeckList(self) :
        print "Count :", len(self.deckList)
        for card in self.deckList :
            card.printCard()

    # This method deals <numCards> cards to player <player> 
    def deal(self, player, numCards): 
        cardList = []
        # Create a list of cards of <numCards> elements and hand it over to the player
        for i in range(0,numCards) :
            cardList.append(self.deckList.pop())
        player.createHand(cardList)

    # This method recives cards back from the players. Currently it only accepts one card but should be modified later to take multiple cards
    def receiveCards(self, card) :
        self.deckList.append(card)

# This class represents each card of the deck
class Card(object) :
    def __init__(self, suit, num) :
        self.suit = suit # suit of the card. The value will be between 0-3 
        self.num = num # card number. Value will be between 1-13

    def printCard(self) :
        print "Suit: {} Number: {}".format(self.suit, self.num)

# This class represents a player
class Player(object) :
    def __init__(self, name) :
        self.name = name
        self.score = 0 
        self.hand = [] # The cards this player gets when the deck is dealt. List of objects of type Card

    def displayPlayer (self) :
         print "Name: {} Score: {}".format(self.name, self.score)
         print "Cards: "
         for i in self.hand :
             i.printCard()

    # This method creates the hand for the player 
    def createHand(self, cards) :
        self.hand = cards
    
    # This method updates the score of the player
    # winOrLoose = True if the game is won, False if the game is lost.
    def updateScore(self, winOrLoose) :
        if (winOrLoose) :
            self.score += 1
        else :
            self.score -= 1

    def discardCard(self) :
        card = self.hand.pop()
        return card
    
# Create a deck object 
deck1 = Deck("dragon")
# Create the initial deck
deck1.createDeckList()
print "Shuffling the cards now"
# Shuffle the deck
deck1.shuffle()

# Create a player 
yukie = Player("Yukie")
yukie.displayPlayer()
# Deal 5 cards to player Yukie
deck1.deal(yukie,5)
deck1.printDeckList()
yukie.displayPlayer()

# Player yukie looses 1 time and wins 2 times. 
yukie.updateScore(False)
yukie.updateScore(True)
yukie.updateScore(True)
yukie.displayPlayer()

# Player yukie discards her card. 
card = yukie.discardCard()
card.printCard()
# Give back the discarded card to deck
deck1.receiveCards(card)
deck1.printDeckList()

# sheetal = Player("sheetal")
# deck1.deal(sheetal,2)
# deck1.printDeckList()

# sheetal.updateScore(True)
# sheetal.updateScore(True)
# sheetal.updateScore(False)
# sheetal.displayPlayer()

# card = sheetal.discardCard()
# card.printCard()
# deck1.receiveCards(card)

