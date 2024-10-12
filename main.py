from GamePlayMoves import GamePlayMoves
from PlayerHand import PlayerHand

def MainGameplayLoop():
    running = True
    MainGame = GamePlayMoves()

    numberOfDecks = int(input("How many Decks would you like to play with? "))

    MainGame.createDeck(numberOfDecks)
    MainGame.randomizeDeck()

    numberOfPlayers = input("How many players are playing??: ")
    chipCount = int(input("How many chips would you like to play with?: "))

    for count in range(int(numberOfPlayers)):
        MainGame.playerHands.append(PlayerHand(int(chipCount), int(count)))

    MainGame.dealToPlayers()
    MainGame.dealToBoard(True)

    while running == True:
        allIn = False
        for player in MainGame.playerHands:
            betRoundResponse = MainGame.betRound(player, allIn)
            if betRoundResponse == "all in":
                allin = True
        for player in MainGame.playerHands:
            if player.lastBetResponse == "all":
                fullDeal = True
            if player.lastBetResponse == "bet":
                singleDeal = True:
        if singleDeal:
            MainGame.dealToBoard(False, )

if __name__ == '__main__':
    MainGameplayLoop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
