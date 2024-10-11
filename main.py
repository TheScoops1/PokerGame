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
        #put main gameplay loop here
        break


if __name__ == '__main__':
    MainGameplayLoop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
