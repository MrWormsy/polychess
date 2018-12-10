# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:35:35 2018

@author: anton
"""

import chess


def getAction(board):
    action = input("Donner une action à réaliser (ex: a2a3) : ")
    try:
        tempMove = chess.Move.from_uci(action)
    except:
        return False
    
    if (tempMove in board.legal_moves):
        return tempMove
    else: False

def main():

    board = chess.Board()
    
    player1 = input("Nom du joueur 1 : ")
    player2 = input("Nom du joueur 2 : ")
    winner = None
    idTour = 0 #Id du tour
    
    #On print le plateau au début
    print(board)
    board
    
    #Tant que un des deux joueurs n'est pas game over
    while(not board.is_game_over()):
        
        #Un joueur choisi une action (on annonce le tour du joueur, si id%2 == 0 alors blanc sinin noir)
        if(idTour%2 == 0):
            print("C'est au tour de", player1)
        else:
            print("C'est au tour de", player2)
        
        #On regarde si l'action est possible et si elle ne l'est pas on lui redemande une action
        action = getAction(board)
        while(action == None):
            print("L'action n'est pas autorisée, veuillez recommencer")
            action = getAction(board)
            
        #Si l'action est possible alors on la réalise
        board.push(action)
    
        #On print le plateau et c'est au joueur suivant de jouer si il n'est pas en echec et mat
        print(board)
        board
        
        #On incremente l'id
        idTour += 1
    
    if (winner == player1):
        print(player1, " a gagné")
    else:
        print(player2, " a gagné")
    
    
if __name__ == "__main__":
    main()  