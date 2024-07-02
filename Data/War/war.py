from random import shuffle

class Card:
    def __init__(self, rank, suit): # constructor
        self.rank = rank
        self.suit = suit

    def setRank(self, rank): # setter
        self.rank = rank # getter
    def getRank(self):
        return self.rank

    def setSuit(self, suit):
        self.suit = suit
    def getSuit(self):
        return self.suit
    
    def __str__(self):
        rank = self.rank
        if(rank == 1):
            rank = "Ace"
        if(rank == 11):
            rank = "Jack"
        if(rank == 12):
            rank = "Queen"
        if(rank == 13):
            rank = "King"
        return str(rank) + " of " + str(self.suit)
    
class Deck:
    def __init__(self, cards):
        self.cards = list(cards)
        self.num_cards = len(self.cards)
    
    def addCard(self, card):
        self.cards.append(card)

    def addCards(self, cards):
        self.cards.extend(cards)

    def removeCard(self, card):
        for c in self.cards:
            if(card.rank == c.rank):
                if(card.suit == c.suit):
                    self.cards.remove(c)
    
    def getCard(self, rank, suit):
        for c in self.cards:
            if(rank == c.rank):
                if(suit == c.suit):
                    return c
    
    def getNumCards(self):
        return len(self.cards)
    
    def makeDefaultDeck(self):
        self.cards = list()
        suits = ["spades", "clubs", "hearts", "diamonds"]
        for s in suits:
            for r in range(1, 14):
                card = Card(r, s)
                self.addCard(card)

    def shuffleDeck(self):
        shuffle(self.cards)

    def popCard(self):
        return self.cards.pop()
    
    def getSplitDeck(self):
        cards1 = self.cards[0:int(len(self.cards) / 2)]
        cards2 = self.cards[int(len(self.cards) / 2):]

        deck1 = Deck(cards1)
        deck2 = Deck(cards2)

        return (deck1, deck2)
        

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck # Deck class
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
    
    def addToStash(self, card):
        if(type(card) == type(list())):
            self.stash.addCards(card)
        else:
            self.stash.addCard(card)
    
    def getNumWins(self):
        return self.num_wins
    
    def drawCard(self):
        return self.deck.popCard()


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
    elif (rank1 == rank2):
        comparison = 0
    else: # rank1 > rank2
        comparison = 1

    return comparison

def war(player1, player2, war_cards1 = list(), war_cards2 = list()):
    # Player 1 wins the game = 1
    # Player 2 wins the game = 2
    # Player 1 wins the war = 3
    # Player 2 wins the war = 4
    player1_deck_length = player1.getDeck().getNumCards()
    player1_stash_length = player1.getStash().getNumCards()
    if(player1_deck_length < 4):
        if((player1_deck_length + player1_stash_length) < 4):
            return 2
    
    player2_deck_length = player2.getDeck().getNumCards()
    player2_stash_length = player2.getStash().getNumCards()
    if(player2_deck_length < 4):
        if((player2_deck_length + player2_stash_length) < 4):
            return 1

    for x in range(0, 4):
        if(player1.getDeck().getNumCards() > 0):
            input("Press 'Enter' to draw")
            war_cards1.append(player1.drawCard())
        else:
            player1.setDeck(player1.getStash())
            player1.getDeck().shuffleDeck()
            player1.setStash(Deck(list()))
            input("Press 'Enter' to draw")
            war_cards1.append(player1.drawCard())
        if(player2.getDeck().getNumCards() > 0):
            war_cards2.append(player2.drawCard())
        else:
            player2.setDeck(player2.getStash())
            player2.getDeck().shuffleDeck()
            player2.setStash(Deck(list()))
            war_cards2.append(player2.drawCard())

    card1 = war_cards1[-1]
    print(player1.getName() + " plays " + str(card1))
    card2 = war_cards2[-1]
    print(player2.getName() + " plays " + str(card2))

    comparison = compareCards(card1, card2)

    if(comparison == 1): # Player 1 wins the round
        print(player1.getName() + " wins the round!")
        player1.addToStash(war_cards1)
        player1.addToStash(war_cards2)
        return 3
    elif(comparison == -1): # Player 2 wins the round
        print(player2.getName() + " wins the round!")
        player2.addToStash(war_cards1)
        player2.addToStash(war_cards2)
        return 4
    else: # War!
        print("War!")
        return war(player1, player2, war_cards1, war_cards2)



gamedeck = initializeDeck()
players = initializePlayers(gamedeck)

while(True):
    if(players[0].getDeck().getNumCards() == 0):
        if(players[0].getStash().getNumCards() == 0):
            print(players[1].getName() + " wins the game!")
            break
        else:
            players[0].setDeck(players[0].getStash())
            players[0].getDeck().shuffleDeck()
            players[0].setStash(Deck(list()))
    if(players[1].getDeck().getNumCards() == 0):
        if(players[1].getStash().getNumCards() == 0):
            print(players[0].getName() + " wins the game!")
            break
        else:
            players[1].setDeck(players[1].getStash())
            players[1].getDeck().shuffleDeck()
            players[1].setStash(Deck(list()))
    input("Press 'Enter' to draw")
    card1 = players[0].drawCard()
    print(players[0].getName() + " drew " + str(card1))
    card2 = players[1].drawCard()
    print(players[1].getName() + " drew " + str(card2))

    comparison = compareCards(card1, card2)

    if(comparison == 1): # Player 1 wins the round
        print(players[0].getName() + " wins the round!")
        players[0].addToStash(card1)
        players[0].addToStash(card2)
    elif(comparison == -1): # Player 2 wins the round
        print(players[1].getName() + " wins the round!")
        players[1].addToStash(card1)
        players[1].addToStash(card2)
    else: # War!
        print("War!")
        winner = war(players[0], players[1], [card1], [card2])
        if(winner == 1):
            print(players[0].getName() + " wins the game!")
            break
        elif(winner == 2):
            print(players[1].getName() + " wins the game!")
            break
        elif(winner == 3):
            print(players[0].getName() + " wins the round!")
        else:
            print(players[1].getName() + " wins the round!")

    print(players[0].getName() + " has " + str(players[0].getDeck().getNumCards() + players[0].getStash().getNumCards()) + " cards")
    print(players[1].getName() + " has " + str(players[1].getDeck().getNumCards() + players[1].getStash().getNumCards()) + " cards")
    print()
