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
        word = self.team + " pawn at " + str(self.row) + "," + str(self.col)
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
        while(i < board.SIZE):
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
        while(i < board.SIZE):
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
        word = self.team + " rook at " + str(self.row) + "," + str(self.col)
        return word


class knight(piece):
    def __init__(self, team, row, col):
        super().__init__(5, team, row, col)
        if self.team == "W":
            self.image = "w_knight.png"
        else:
            self.image = "b_knight.png"

    def getMoves(self, board):
        r = self.row
        c = self.col
        validMoves = []
        if(r - 2 >= 0 and c - 1 >= 0):
            validMoves.append(board.table[r-2][c-1])
        if(r - 2 >= 0 and c + 1 < len(board.table[0])):
            validMoves.append(board.table[r-2][c+1])
        if(r + 2 < len(board.table) and c - 1 >= 0):
            validMoves.append(board.table[r+2][c-1])
        if(r + 2 < len(board.table) and c + 1 < len(board.table[0])):
            validMoves.append(board.table[r+2][c+1])
        return validMoves

    def __str__(self):
        word = self.team + "knight at " + str(self.row) + "," + str(self.col)
        return word


class bishop(piece):
    def __init__(self, team, row, col):
        super().__init__(5, team, row, col)
        if self.team == "W":
            self.image = "w_bishop.png"
        else:
            self.image = "b_bishop.png"

    def getMoves(self, board):
        r = self.row
        c = self.col
        validMoves = []
        r1 = r - 1
        c1 = c - 1
        while c1 >= 0 and r1 >= 0:
            if board.table[r1][c1].occupiedBy != None:
                if board.table[r1][c1].occupiedBy.team != self.team:
                    validMoves.append(board.table[r1][c1])
                    break
                else:
                    break
            validMoves.append(board.table[r1][c1])
            c1 = c1 - 1
            r1 = r1 - 1

        r1 = r - 1
        c1 = c + 1
        while c1 < len(board.table[0]) and r1 >= 0:
            if board.table[r1][c1].occupiedBy != None:
                if board.table[r1][c1].occupiedBy.team != self.team:
                    validMoves.append(board.table[r1][c1])
                    break
                else:
                    break
            validMoves.append(board.table[r1][c1])
            c1 = c1 + 1
            r1 = r1 - 1

        r1 = r + 1
        c1 = c - 1
        while r1 < len(board.table[0]) and c1 >= 0:
            if board.table[r1][c1].occupiedBy != None:
                if board.table[r1][c1].occupiedBy.team != self.team:
                    validMoves.append(board.table[r1][c1])
                    break
                else:
                    break
            validMoves.append(board.table[r1][c1])
            c1 = c1 - 1
            r1 = r1 + 1

        r1 = r + 1
        c1 = c + 1
        while c1 < len(board.table[0]) and r1 < len(board.table[0]):
            if board.table[r1][c1].occupiedBy != None:
                if board.table[r1][c1].occupiedBy.team != self.team:
                    validMoves.append(board.table[r1][c1])
                    break
                else:
                    break
            validMoves.append(board.table[r1][c1])
            c1 = c1 + 1
            r1 = r1 + 1
        return validMoves

    def __str__(self):
        word = self.team + "bishop at " + str(self.row) + "," + str(self.col)
        return word


class queen(piece):
    def __init__(self, team, row, col):
        super().__init__(5, team, row, col)
        if self.team == "W":
            self.image = "w_queen.png"
        else:
            self.image = "b_queen.png"

    def getMoves(self, board):
        r = self.row
        c = self.col
        validMoves = []
        r1 = r - 1
        c1 = c - 1
        while c1 >= 0 and r1 >= 0:
            if board.table[r1][c1].occupiedBy != None:
                if board.table[r1][c1].occupiedBy.team != self.team:
                    validMoves.append(board.table[r1][c1])
                    break
                else:
                    break
            validMoves.append(board.table[r1][c1])
            c1 = c1 - 1
            r1 = r1 - 1

        r1 = r - 1
        c1 = c + 1
        while c1 < len(board.table[0]) and r1 >= 0:
            if board.table[r1][c1].occupiedBy != None:
                if board.table[r1][c1].occupiedBy.team != self.team:
                    validMoves.append(board.table[r1][c1])
                    break
                else:
                    break
            validMoves.append(board.table[r1][c1])
            c1 = c1 + 1
            r1 = r1 - 1

        r1 = r + 1
        c1 = c - 1
        while r1 < len(board.table[0]) and c1 >= 0:
            if board.table[r1][c1].occupiedBy != None:
                if board.table[r1][c1].occupiedBy.team != self.team:
                    validMoves.append(board.table[r1][c1])
                    break
                else:
                    break
            validMoves.append(board.table[r1][c1])
            c1 = c1 - 1
            r1 = r1 + 1

        r1 = r + 1
        c1 = c + 1
        while c1 < len(board.table[0]) and r1 < len(board.table[0]):
            if board.table[r1][c1].occupiedBy != None:
                if board.table[r1][c1].occupiedBy.team != self.team:
                    validMoves.append(board.table[r1][c1])
                    break
                else:
                    break
            validMoves.append(board.table[r1][c1])
            c1 = c1 + 1
            r1 = r1 + 1
        i = r + 1
        while(i < board.SIZE):
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
        while(i < board.SIZE):
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
        word = self.team + "bishop at " + str(self.row) + "," + str(self.col)
        return word


class king(piece):
    def __init__(self, team, row, col):
        super().__init__(5, team, row, col)
        if self.team == "W":
            self.image = "w_king.png"
        else:
            self.image = "b_king.png"

    def getMoves(self, board):
        r = self.row
        c = self.col
        validMoves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if r + i >= 0 and r + i < len(board.table) and c + j >= 0 and c + j < len(board.table[0]):
                    if board.table[r+i][j+c].occupiedBy != None and board.table[r+i][j+c].occupiedBy.team == self.team:
                        continue
                    else:
                        validMoves.append(board.table[r+i][j+c])
        return validMoves
