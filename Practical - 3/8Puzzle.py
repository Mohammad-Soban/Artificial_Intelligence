import numpy as NumPY
from datetime import datetime
from BFSFor8Puzzle import BFSFor8Puzzle
from DFSFor8Puzzle import DFSFor8Puzzle

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


initialstate = []
goalstate = []


print("21BCP448D: Jainil Prajapati")

print("Example: 1 2 3 4 5 6 7 8 s \n")
print("Note that s is used to represent the empty space\n--------------------------\n")

# For initalstate input
print("Enter The initial state of 8 Puzzle: \n")
ele = input().strip().split(" ")
initialstate.append(ele)

# For Goalstate input
print("Enter The goal state of 8 Puzzle: \n")
ele = input().strip().split(" ")
goalstate.append(ele)


# For converting the input into 2D array
initialstate = NumPY.array(initialstate).reshape(3,3)
goalstate = NumPY.array(goalstate).reshape(3,3)



# For choosing the method for solving the 8 puzzle
print("By Which Method You Want To Solve The 8 Puzzle?\n")
print("1. BFS\n2. DFS\n")

choice = int(input())

print("Current Time =", current_time)

if(choice == 1):
    BFSFor8Puzzle(initialstate.tolist(),goalstate.tolist())
else:
    DFSFor8Puzzle(initialstate.tolist(),goalstate.tolist())

print("Current Time =", current_time)
