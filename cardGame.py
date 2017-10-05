from random import shuffle

class Deck(object) :
    def __init__(self, picture) :
        self.picture = picture
        self.totalCards = 52
        self.deckList = []

    
    def createDeckList(self) :
        for i in range(0,4) :
            for j in range(1,14) :
                card = Card(i,j)
                self.deckList.append(card)
        return self
    
    def shuffle(self) :
        shuffle(self.deckList)
        return self
    
    def printDeckList(self) :
        print "Count :", len(self.deckList)
        for card in self.deckList :
            card.printCard()
            
    def deal(self, player, numCards): 
        cardList = []
        for i in range(0,numCards) :
            cardList.append(self.deckList.pop())
        player.createHand(cardList)

    def receiveCards(self, card) :
        self.deckList.append(card)

class Card(object) :
    def __init__(self, suit, num) :
        self.suit = suit
        self.num = num

    def printCard(self) :
        print "Suit: {} Number: {}".format(self.suit, self.num)

class Player(object) :
    def __init__(self, name) :
        self.name = name
        self.score = 0
        self.hand = []

    def displayPlayer (self) :
         print "Name: {} Score: {}".format(self.name, self.score)
         print "Cards: "
         for i in self.hand :
             i.printCard()
    
    def createHand(self, cards) :
        self.hand = cards
    
    def updateScore(self, winOrLoose) :
        if (winOrLoose) :
            self.score += 1
        else :
            self.score -= 1

    def discardCard(self) :
        card = self.hand.pop()
        return card
    

deck1 = Deck("dragon")
deck1.createDeckList()
print "Shuffling the cards now"
deck1.shuffle()

yukie = Player("Yukie")
yukie.displayPlayer()
deck1.deal(yukie,5)
deck1.printDeckList()
yukie.displayPlayer()

yukie.updateScore(False)
yukie.updateScore(True)
yukie.updateScore(True)
yukie.displayPlayer()

card = yukie.discardCard()
card.printCard()
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

