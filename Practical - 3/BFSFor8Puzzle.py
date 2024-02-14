from CheckMoveAvalibility import checkForAvailableMove
from ApplyMoves import ApplyMoves
import numpy as NumPY

def BFSFor8Puzzle(InitialState:list,GoalState:list):

    if isinstance(InitialState,list) == False:
        return False

    queue = [(InitialState,[])]
    visited = []

    while queue:    

        CurrentState = queue.pop(0)

        EmptyMovePosition = NumPY.argwhere(NumPY.array(CurrentState[0]) == 's')

        moves = checkForAvailableMove(CurrentState[0],EmptyMovePosition)
        APM = ApplyMoves(CurrentState,moves,EmptyMovePosition)

        for state in APM:

            # print(state)
            if (state[0] == GoalState):
                print("Goal State Found")
                print(state[1])
                return True

            if state[0] not in visited and state[0] not in queue:
                queue.append(state)

        visited.append(CurrentState)

