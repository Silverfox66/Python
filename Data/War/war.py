from random import shuffle

class Card:
    def __init__(self, rank, suit, ):
        self.rank = suit
        self.suit = suit

    def setRank(self, rank):
        self.rank= rank
    def getRank(self):
        return self.rank

    def setSuit(self, suit):
        self.suit = suit
    def getSuit(self):
        return self.suit

class Deck:
    def __init__(self, cards):
        self.card = list(cards)
        self.num_cards = len(self.cards)

    def addCard(self, card):
        self.cards.append(card)

    def makeDefaultDeck(self):
        suits = ["spades", "clubs", "diamonds", "hearts"]
        for s in suits:
            for r in range(1, 14):
                card = Card(r, s)
                self.addCard(card)
    
    def shuffleDeck(self):
        self.cards = shuffle(self.cards)

    def popCard(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, deck,):
        self.name = name
        self.deck = deck
        self.num_wins = 0

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    
    def setDeck(self, deck):
        self.deck = deck
    def getDeck(self):
        return self.deck
    
    def getNumWins(self):
        return self.num_wins
    
    def drawCard(self):
        return self.deck.popCard()
    

class War:
    def __init__(self, deck, player1, player2):
        self.deck = deck
        self.player1 = player1
        self.player2 = player2
        self.is_war = False
        self.game_over = False
    
    def setDeck(self, deck):
        self.deck = deck
    def getDeck(self):
        return self.deck
    
    def setPlayers(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    def getPlayers(self):
        return (self.player1, self.player2)
    def getIsWar(self):
        return self.is_war
    def getGameOver(self):
        return self.game_over
    def dealCards(self):
        pass


def initializeDeck():
    game_deck = Deck(list())
    game_deck.makeDefaultDeck()
    game_deck.shuffleDeck()

    return game_deck

def initializePlayers(game_deck):
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")


card = Card(3, "hearts")
card.rank = 5
card.setRank(5)