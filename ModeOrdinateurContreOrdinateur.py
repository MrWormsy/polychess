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