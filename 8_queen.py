import random

class EightQueen:
    def __init__(self, board):
        #initial puzzle
        self.board = board
        self.complete = True

    def get_h_cost(self):
        h = 0
        for i in range(len(board)):
            #Check every column we haven't already checked
            for j in range(i + 1,len(board)):
                #Queens are in the same row
                if board[i] == board[j]:
                    h += 1

                #Get the difference between the current column
                #and the check column
                offset = j - i
                #To be a diagonal, the check column value has to be 
                #equal to the current column value +/- the offset
                if board[i] == board[j] - offset or board[i] == board[j] + offset:
                    h += 1
        return h

    def make_move_steepest_hill(self):
        board = self.board
        h_to_beat = EightQueen.get_h_cost(board)
        if h_to_beat == 0:
            self.complete = False
            return board
        moves = {}
        for col in range(len(board)):

            for row in range(len(board)):
                if board[col] == row:
                    #We don't need to evaluate the current
                    #position, we already know the h-value
                    continue
        
                board_copy = list(board)
                #Move the queen to the new row
                board_copy[col] = row
                moves[(col,row)] = EightQueen.get_h_cost(board_copy)
        best_moves = []
        for move,h_cost in moves.items():
            if h_cost < h_to_beat:
                h_to_beat = h_cost
        
        for move,h_cost in moves.items():
            if h_cost == h_to_beat:
                best_moves.append(move)

        #Pick a random best move
        if len(best_moves) > 0:
            pick = random.randint(0,len(best_moves) - 1)
            col = best_moves[pick][0]
            row = best_moves[pick][1]
            board[col] = row

        return board

    def solve_board(self):
        i = 0
        while self.complete:
            move = EightQueen.make_move_steepest_hill(self)
            i += 1
            print("Move " + str(i))
            print(move)

if __name__ == "__main__":
    board = [0,0,1,2,4,3]
    print("Problem")
    print(board)
    out = EightQueen(board)
    out.solve_board()
