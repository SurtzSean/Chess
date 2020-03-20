import random


class AI:
    def __init__(self, data, board, player):
        self.data = data
        self.player = player
        self.board = board
        self.gm = player.gm

    def move(self):
        piece = random.choice(self.player.pieces)
        while len(piece.getMoves(self.board)) == 0:
            piece = random.choice(self.player.pieces)
        move = random.choice(piece.getMoves(self.board))
        self.player.movePiece(self.board, piece, move.row, move.col)

    def pickMove(self):
        import math


def minimax(curDepth, nodeIndex,
            maxTurn, scores,
            targetDepth):

    # base case : targetDepth reached
    if (curDepth == targetDepth):
        return scores[nodeIndex]

    if (maxTurn):
        return max(minimax(curDepth + 1, nodeIndex * 2,
                           False, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                           False, scores, targetDepth))

    else:
        return min(minimax(curDepth + 1, nodeIndex * 2,
                           True, scores, targetDepth),
                   minimax(curDepth + 1, nodeIndex * 2 + 1,
                           True, scores, targetDepth))
