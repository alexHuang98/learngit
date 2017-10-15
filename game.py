import random
import faan as fn

class Game(object):
    def __init__(self, nbDealer, nbPrevailingWind, nbGames):
        self.nbDealer = nbDealer
        self.nbPrevailingWind = nbPrevailingWind
        self.gameInfo = self.newGame(nbDealer, nbPrevailingWind, nbGames)
        self.ifEnd = False
        #self.tiles = self.getInitTiles()

    def newGame(self, nbDealer, nbPrevailingWind, nbGames): # launch a new game, returns all game info
        gameInfo = {}
        gameInfo['nbGames'] = nbGames
        gameInfo['turn'] = 0 # number of decision-maker
        tiles = self.getInitTiles() # get randomly ordered tiles
        gameInfo['dealer'] = nbDealer # the number of dealer who is the East
        gameInfo['prevailingWind'] = nbPrevailingWind # start from east, changes every 4 games
        gameInfo['tilePos'] = (52, 143)
        gameInfo['tiles'] = tiles
        # initialization for tiles
        gameInfo['handTiles'] = [None, None, None, None]
        for i in range(0, 4):
            for j in range(i*13, i*13+13):
                gameInfo['handTiles'][i].append((tiles[j], 0)) # 0:hand tiles, 1,2,3,4: the ith eaten/pong, 5 hidden kong, 6 flowers
        gameInfo['historyActions'] = [] # (i, j, k) i: which player, j:action(eaten, pong, kong, play), k:which tile
        return gameInfo


    #【改】play只监听状态，具体的流程等等要写在更上层，例：主测试函数中
    def play(self):
        print("Game starts")
        while(True):
            # user's turn
            historyTiles = self.gameInfo['historyTiles'].sort()
            tiles = self.gameInfo['handTiles'][0] + self.gameInfo['wallTiles'][0]
            self.gameInfo['wallTiles'].remove(tiles[-1])
            handTiles = tiles[0].sort()
            tilesEaten = tiles[1]
            pongs = tiles[2]
            kongs = tiles[3]
            hiddenKongs = tiles[4]
            print("Your hand tiles:"+str(handTiles))
            print("Your tiles eaten:"+str(tilesEaten))
            print("Your pongs:"+str(pongs))
            print("Your kongs:"+str(kongs))
            print("Your hidden kongs:"+str(hiddenKongs))
            if self.result(handTiles, tilesEaten, pongs, kongs, hiddenKongs) > 0:
                decision = input("You can win "+str(self.result(handTiles))+", please decide whether to finish. N: not finish; Y: finish now")
                if str(decision) == 'Y':
                    print("Game finished. You win "+str(self.result(handTiles))+" points")
                    break
            handTiles, pongs, kongs, hiddenKongs = self.ifGetKong(handTiles, pongs, kongs, hiddenKongs)
            indice = int(input("Please enter the indice of the tile you want to throw"))
            while(True):
                if indice >= 0 and indice < len(handTiles):
                    break
                print("Invalid indice. Please enter it again")
                indice = int(input("Please enter the indice of the tile you want to throw"))
            tileThrown = handTiles[indice]
            self.historyTiles += tileThrown
            handTiles.remove(tileThrown)
            # computer's turn

    def result(self):
        faans = []
        return faans # score of 4 players

    def score(self, lastGetTile):
        #先判断胡没胡，再判断多少番
        N = 60 # number of faans
        flag = []
        faan = 0
        if fn.FAANS[0][2](self.gameInfo):
            for i in range(0, N):
                if fn.FAANS[i][2](self.gameInfo, lastGetTile):
                    flag.apppend(True)
                else:
                    flag.apppend(False)
        # check the flags to calculate final faan
        #[to to]
        return faan # return the faan calculated

    def ifGetKong(self, handTiles, pongs, kongs, hiddenKongs): # if
        newHandTiles = handTiles
        newPongs = pongs
        newKongs = kongs
        newHiddenKongs = hiddenKongs
        return newHandTiles, newPongs, newKongs, newHiddenKongs

    def getInitTiles(self): # get an array of randomly ordered tiles
        tiles = []
        dots = [] # tong
        bamboos = [] # tiao
        characters = [] # wan
        winds = [] # feng
        dragons = [] # zhong fa bai
        for i in range(0, 4):
            dots += [1,2,3,4,5,6,7,8,9]
            bamboos += [11,12,13,14,15,16,17,18,19]
            characters += [21,22,23,24,25,26,27,28,29]
            winds += [31, 32, 33, 34]
            dragons += [41, 42, 43]
            flowers = [51,52,53,54,55,56,57,58]
        tiles = dots + bamboos + characters + winds + dragons
        random.shuffle(tiles)
        return tiles
