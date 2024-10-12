import random

from Cards import Card

class GamePlayMoves:

    def __init__(self):
        self.deckList = []
        self.mainHand = []
        self.board = []
        self.playerHands = []
        self.betPot = 0
        pass

    def createDeck(self, DeckVolume: int):
        for count in range(DeckVolume):
            for cardCreation in range(13):
                self.deckList.append(Card(cardCreation, 'Spade'))
                self.deckList.append(Card(cardCreation, 'Heart'))
                self.deckList.append(Card(cardCreation, 'Club'))
                self.deckList.append(Card(cardCreation, 'Diamond'))

    def randomizeDeck(self):
        random.shuffle(self.deckList)

    def dealToPlayers(self):
        dealtCardCount = 2
        totalPlayers = len(self.playerHands)
        finished = False

        while not finished:
            for playerCount in range(totalPlayers):
                for cardCount in range(dealtCardCount):
                    self.playerHands[playerCount - 1].hand.append(self.deckList.pop())
            if len(self.playerHands[0].hand) == dealtCardCount:
                finished = True

    def dealToBoard(self, firstDeal: bool, fullDeal: bool):
        if firstDeal:
            for count in range(3):
                self.board.append(self.deckList.pop())
        elif fullDeal:
            for count in range(2):
                self.board.append(self.deckList.pop())
        else:
            self.board.append(self.deckList.pop())

    def betRound(self, player: object, allIn: bool):
        if allIn is True:
            response = input("Player " + str(player.playerCount) + " would you like to go all in or fold?")
            if response == "all":
                self.betPot += player.chipCount
                player.chipCount = 0
            if response == "fold":
                player.playerHandStatus = "loser"
        else:
            response = input("Player " + str(player.playerCount) + " Would you like to check, bet, fold or go all in? (type all for all in)")
            if response == "check":
                player.lastBetResponse = response
                check = "check"
                return check
            if response == "bet":
                player.lastBetResponse = response
                betAmount = int(input("Player " + str(player.playerCount) + " How much would you like to bet?"))
                self.betPot += int(betAmount)
                player.chipCount -= int(betAmount)
                bet = "bet"
                return bet
            if response == "fold":
                player.lastBetResponse = response
                player.playerHandStatus = "loser"
                fold = "fold"
                return fold
            if response == "all":
                player.lastBetResponse = response
                self.betPot += player.chipCount
                player.chipCount = 0
                allIn = "all in"
                return allIn
