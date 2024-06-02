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
    
    def getSplitDeck(self):
        cards1 = self.cards[0:int(len(self.cards) / 2)]
        cards2 = self.cards[int(len(self.cards) / 2):]

        deck1 = Deck(cards1)
        deck2 = Deck(cards2)

        return (deck1, deck2)


class Player:
    def __init__(self, name, deck,):
        self.name = name
        self.deck = deck
        self.stash = Deck(list())
        self.num_wins = 0

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    
    def setDeck(self, deck):
        self.deck = deck
    def getDeck(self):
        return self.deck
    
    def setStash(self, stash):
        self.stash = stash
    def getStash(self):
        return self.stash
    
    def addToStash(self,card):
        self.stash.addCard(card)
    
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


    (player1_deck, player2_deck) = game_deck.getSplitDeck()

    player1 = Player(player1_name, player1_deck)
    player2 = Player(player2_name, player2_deck)


    return (player1, player2)

def compareCards(card1, card2):
    rank1 = card1.getRank()
    rank2 = card2.getRank()

    if(rank1 == 1):
        rank1 = 14
    if(rank2 == 1):
        rank2 = 14
    
    comparison = None

    if(rank1 < rank2):
        comparison = -1
    elif(rank1 == rank2):
        comparison = 0
    else:
        comparison = 1
    
    return comparison


gamedeck = initializeDeck
players = initializePlayers(gamedeck)

while(True):
    card1 = players[0].drawCard()
    card2 = players[1].drawCard()

    comparison = compareCards(card1, card2) 

    if(comparison == 1):
        card1 + card2
    elif(comparison == -1):
        card1 + card2
    else:
        pass




card = Card(3, "hearts")
card.rank = 5
card.setRank(5)