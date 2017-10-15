FAANS = [
("IfScored", 0, FAANS_Scored),
("BigFour", 88, FAANS_BigFourWinds)
]

# if one can score
def FAANS_IfScored(gameInfo):
    flag = False
    return flag


# 88 points
def FAANS_BigFourWinds(gameInfo, lastGetTile): # lastGetTile(i, j) i:which tile, j:how someone get this tile
    flag = False
    if len(handTiles) == 141:
        flag = True
    return flag

# 64 points
