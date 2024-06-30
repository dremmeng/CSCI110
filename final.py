#Drew Remmenga
#All games of tic tack toe
import json
import unittest
with open(r"C:\Users\Drewr\Documents\School\CSCI110\Final\axes.txt") as f:
    axes = json.load(f)
f.close()

def isWin(board):
    return any("".join(board[p] for p in axis) in ["XXX", "OOO"] for axis in axes)


def validBoards(board="."*9, player=None):
    if player == None:
        yield board  # count the empty board
        for b in validBoards(board, player="X"):
            yield b  # X goes 1st
        for b in validBoards(board, player="O"):
            yield b  # O goes 1st
        return
    opponent = "XO"[player == "X"]
    for pos, cell in enumerate(board):
        if cell != ".":
            continue
        played = board[:pos]+player+board[pos+1:]  # simulate move
        yield played                              # return the new state
        if isWin(played):
            continue                # stop game upon winning
        for nextBoard in validBoards(played, opponent):
            yield nextBoard  # return boards for subsequent moves


f = open(r"C:\Users\Drewr\Documents\School\CSCI110\Final\Boards.txt", "w")

distinctBoards = set(validBoards())  # only look at distinct board states
f.write("Distinct Boards: "+str(len(distinctBoards))+"\n")

winningStates = sum(isWin(b) for b in distinctBoards)
f.write("Winning boards: " + str(winningStates)+"\n")  # 1884  (so 942 for a specific starting player)

filledStates = sum(("." not in b) for b in distinctBoards)
f.write("Filled Boards: " + str(filledStates)+"\n")  # 156 states where all cells are filled

finalStates = sum(isWin(b) or ("." not in b) for b in distinctBoards)
f.write("Final Boards: "+ str(finalStates)+"\n")  # 1916 end of game states (win or draw)

earlyWins = sum(isWin(b) and ("." in b) for b in distinctBoards)
f.write("Early Wins: "+ str(earlyWins)+"\n")  # 1760 wins before filling the board

draws = finalStates - winningStates
f.write("Draws: "+ str(draws)+"\n")  # 32 ways to end up in a draw
lastWins = filledStates-draws
f.write("Wins on the last move: "+ str(lastWins)+"\n")  # 124 wins on the 9th move (i.e filling the board)

fastWins = sum(isWin(b) and b.count(".") == 4 for b in distinctBoards)
f.write("Fast wins: "+str(fastWins)+"\n")  # 240 fastest wins by 1st player (in 3 moves)

fastCounters = sum(isWin(b) and b.count(".") == 3 for b in distinctBoards)
f.write("Fast Counters: "+str(fastCounters)+"\n")  # 296 fastest wins by 2nd player (in 3 moves)
f.close()
assert (isWin("XXOXOXXXOX"), True)
assert (isWin("XOOOXOOXX"), False)
