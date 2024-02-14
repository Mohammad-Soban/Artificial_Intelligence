import numpy as NumPY
import copy

def ApplyMoves(State: tuple, moves: list, SpacePosition: NumPY.ndarray):
    if not isinstance(State, tuple) or not isinstance(moves, list):
        return False
    
    SpacePosition = SpacePosition[0]

    Combinations = []

    for move in moves:
        if CheckForDuplicateState(State, move) or CheckForOppositeMove(State, move):
            continue

        TempState = copy.deepcopy(State[0])

        TempState[SpacePosition[0]][SpacePosition[1]] = TempState[move[1][0]][move[1][1]]
        TempState[move[1][0]][move[1][1]] = "s"

        NextSeq = State[1] + [(TempState[SpacePosition[0]][SpacePosition[1]], move[0])]

        Combinations.append((TempState, NextSeq))

    return Combinations

def CheckForDuplicateState(State, move):
    return State[1].__len__() > 0 and State[1][-1][1] == move[1]

def CheckForOppositeMove(State, move):
    if State[1].__len__() > 0:
        last_move = State[1][-1]
        return last_move[0] == move[0] and abs(last_move[1] - move[1]) == 2
    return False
