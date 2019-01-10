# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 08:33:31 2018

@author: anton
"""

import chess

class ModeOrdinateurContreOrdinateur:
    
    def __init__(self):
        self.nameAI1 = "AI Missy"
        self.nameAI2 = "AI MrWormsy"
        self.turnId = 0
        
        self.board = chess.Board()
        
        #We print the board
        print(self.board)
        
    def commencerPartie(self):
        
        
        while(self.partieEstFinie()):
            
            self.notificationTourJoueur()
                
            #Si l'action est possible alors on la réalise
            self.board.push(self.getAction())
        
            #On print le plateau et c'est au joueur suivant de jouer si il n'est pas en echec et mat
            print(self.board)
            
            #On incremente l'id
            self.turnId += 1
            
        self.finDePartie()
        
    def notificationTourJoueur(self):
        #Un joueur choisi une action (on annonce le tour du joueur, si id%2 == 0 alors blanc donc joueur sinon noir)
        if(self.turnId%2 == 0):
            print("C'est au tour de", self.nameAI1)
        else:
            print("C'est au tour de", self.nameAI2)
        
    def minimaxRoot(depth, board,isMaximizing):
        possibleMoves = board.legal_moves
        bestMove = -9999
        bestMoveFinal = None
        for x in possibleMoves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            value = max(bestMove, ModeOrdinateurContreOrdinateur.minimax(depth - 1, board,-10000,10000, not isMaximizing))
            board.pop()
            if( value > bestMove):
                print("Best score: " ,str(bestMove))
                print("Best move: ",str(bestMoveFinal))
                bestMove = value
                bestMoveFinal = move
        return bestMoveFinal
    
    def minimax(depth, board, alpha, beta, is_maximizing):
        if(depth == 0):
            return -ModeOrdinateurContreOrdinateur.evaluation(board)
        possibleMoves = board.legal_moves
        if(is_maximizing):
            bestMove = -9999
            for x in possibleMoves:
                move = chess.Move.from_uci(str(x))
                board.push(move)
                bestMove = max(bestMove,ModeOrdinateurContreOrdinateur.minimax(depth - 1, board,alpha,beta, not is_maximizing))
                board.pop()
                alpha = max(alpha,bestMove)
                if beta <= alpha:
                    return bestMove
            return bestMove
        else:
            bestMove = 9999
            for x in possibleMoves:
                move = chess.Move.from_uci(str(x))
                board.push(move)
                bestMove = min(bestMove, ModeOrdinateurContreOrdinateur.minimax(depth - 1, board,alpha,beta, not is_maximizing))
                board.pop()
                beta = min(beta,bestMove)
                if(beta <= alpha):
                    return bestMove
            return bestMove
    
    
    def calculateMove(board):
        possible_moves = board.legal_moves
        if(len(possible_moves) == 0):
            print("No more possible moves...Game Over")
        bestMove = None
        bestValue = -9999
        for x in possible_moves:
            move = chess.Move.from_uci(str(x))
            board.push(move)
            boardValue = -ModeOrdinateurContreOrdinateur.evaluation(board)
            board.pop()
            if(boardValue > bestValue):
                bestValue = boardValue
                bestMove = move
    
        return bestMove
    
    def evaluation(board):
        i = 0
        evaluation = 0
        x = True
        try:
            x = bool(board.piece_at(i).color)
        except:
            x = x
        while i < 63:
            i += 1
            evaluation = evaluation + (ModeOrdinateurContreOrdinateur.getPieceValue(str(board.piece_at(i))) if x else -ModeOrdinateurContreOrdinateur.getPieceValue(str(board.piece_at(i))))
        return evaluation
    
    
    def getPieceValue(piece):
        if(piece == None):
            return 0
        value = 0
        if piece == "P" or piece == "p":
            value = 10
        if piece == "N" or piece == "n":
            value = 30
        if piece == "B" or piece == "b":
            value = 30
        if piece == "R" or piece == "r":
            value = 50
        if piece == "Q" or piece == "q":
            value = 90
        if piece == 'K' or piece == 'k':
            value = 900
        #value = value if (board.piece_at(place)).color else -value
        return value
    """
    def getAction(self):
        bestMove = ""
        with chess.polyglot.open_reader("bookfish.bin") as reader:
            for entry in reader.find_all(self.board):
                bestMove = entry.move().__str__()
                break
        
        #Player
        if(self.turnId%2 == 0):
            print(self.nameAI1 + " a joue " + bestMove)
            return chess.Move.from_uci(bestMove)
        else:
            print(self.nameAI2 + " a joue " + bestMove)
            return chess.Move.from_uci(bestMove)
    """
    
    def getAction(self):
        
        move = ModeOrdinateurContreOrdinateur.minimaxRoot(3,self.board,True)
        
        #Player
        if(self.turnId%2 == 0):
            print(self.nameAI1 + " a joue " + str(move))
            return move
        else:
            print(self.nameAI2 + " a joue " + str(move))
            return move
        
    def moveEstLegal(self, action):
        try:
            tempMove = chess.Move.from_uci(action)
        except:
            return False
        
        if (tempMove in self.board.legal_moves):
            return True
        else: return False
        
        
    def partieEstFinie(self):
        return not self.board.is_game_over()
    
    def finDePartie(self):
        if (self.turnId%2 == 0):
            print(self.nameAI1, " a gagné")
        else:
            print(self.nameAI2, " a gagné")