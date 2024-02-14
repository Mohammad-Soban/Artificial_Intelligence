import numpy as NumPY

def checkForAvailableMove(State:NumPY.ndarray,SpacePosition:NumPY.ndarray):

    X,Y = SpacePosition.tolist()[0]

    moves = []

    if X+1 < State.__len__():
        moves.append(("up",[X+1,Y]))

    if Y+1 < State[0].__len__():
        moves.append(("left",[X,Y+1]))

    if X-1 >= 0:
        moves.append(("down",[X-1,Y]))

    if Y-1 >= 0 :
        moves.append(("right",[X,Y-1]))

    return moves


# 1 2 3
# 4 s 5
# 6 7 8

# --------------------------
# state1     state2      state3     state4
# 1 2 3      1 2 3       1 s 3      1 2 3
# 4 5 s      s 4 5       4 2 5      4 7 5  
# 6 7 8      6 7 8       6 7 8      6 s 8

# state4.1
# 1 2 3
#  
# 

# 1 2 3
# 4 5 6
# s 7 8