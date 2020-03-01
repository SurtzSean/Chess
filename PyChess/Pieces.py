class piece():
    def __init__(self, value, team, row, col):
        self.value = value
        self.team = team
        self.row = row
        self.col = col


class pawn(piece):
    def __init__(self, team,  row, col):
        super().__init__(1, team, row, col)
        if self.team == "W":
            self.image = "w_pawn.png"
        else:
            self.image = "b_pawn.png"
        self.firstMove = True

    def getMoves(self, board):
        validMoves = []
        r = self.row
        c = self.col
        max_dist = 1
        if self.team == 'B':
            if(self.firstMove and board.table[r-2][c].occupiedBy == None):
                validMoves.append(board.table[r-2][c])
            if(r > 0 and board.table[r-1][c].occupiedBy == None):
                validMoves.append(board.table[r-1][c])
            if(r > 0 and c > 0 and board.table[r-1][c-1].occupiedBy != None and board.table[r-1][c-1].occupiedBy.team != self.team):
                validMoves.append(board.table[r-1][c-1])
            if(r > 0 and c < board.SIZE - 1 and board.table[r-1][c+1].occupiedBy != None and board.table[r-1][c+1].occupiedBy.team != self.team):
                validMoves.append(board.table[r-1][c+1])

        if self.team == 'W':
            if(self.firstMove and board.table[r+2][c].occupiedBy == None):
                validMoves.append(board.table[r+2][c])
            if(r < board.SIZE - 1 and board.table[r+1][c].occupiedBy == None):
                validMoves.append(board.table[r+1][c])
            if(r < board.SIZE - 1 and c < board.SIZE - 1 and board.table[r+1][c+1].occupiedBy != None and board.table[r+1][c+1].occupiedBy.team != self.team):
                validMoves.append(board.table[r+1][c+1])
            if(r < board.SIZE - 1 and c > 0 and board.table[r+1][c-1].occupiedBy != None and board.table[r+1][c-1].occupiedBy.team != self.team):
                validMoves.append(board.table[r+1][c-1])
        return validMoves

    def __str__(self):
        word = "pawn at " + str(self.row) + "," + str(self.col)
        return word


class rook(piece):
    def __init__(self, team, row, col):
        super().__init__(5, team, row, col)
        if self.team == "W":
            self.image = "w_rook.png"
        else:
            self.image = "b_rook.png"

    def getMoves(self, board):
        r = self.row
        c = self.col
        validMoves = []
        i = r + 1
        while(i < board.SIZE - 1):
            if(board.table[i][c].occupiedBy != None):
                if board.table[i][c].occupiedBy.team == self.team:
                    break
                else:
                    validMoves.append(board.table[i][c])
                    break
            validMoves.append(board.table[i][c])
            i += 1
        i = r - 1
        while(i > 0):
            if(board.table[i][c].occupiedBy != None):
                if board.table[i][c].occupiedBy.team == self.team:
                    break
                else:
                    validMoves.append(board.table[i][c])
                    break
            validMoves.append(board.table[i][c])
            i -= 1
        i = c + 1
        while(i < board.SIZE - 1):
            if(board.table[r][i].occupiedBy != None):
                if board.table[r][i].occupiedBy.team == self.team:
                    break
                else:
                    validMoves.append(board.table[r][i])
                    break
            validMoves.append(board.table[r][i])
            i += 1
        i = c - 1
        while(i > 0):
            if(board.table[r][i].occupiedBy != None):
                if board.table[r][i].occupiedBy.team == self.team:
                    break
                else:
                    validMoves.append(board.table[r][i])
                    break
            validMoves.append(board.table[r][i])
            i -= 1
        return validMoves

    def __str__(self):
        word = "rook at " + str(self.row) + "," + str(self.col)
        return word
