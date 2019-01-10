# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:35:35 2018

@author: MrWormsy
"""

from ModeJoueurContreJoueur import ModeJoueurContreJoueur
from ModeJoueurContreOrdinateur import ModeJoueurContreOrdinateur
from ModeOrdinateurContreOrdinateur import ModeOrdinateurContreOrdinateur
import Utils

import chess

def main():
    choixModeDeJeu()

def choixModeDeJeu():
    inputStr = input("Mode joueur vs joueur (1) ou Mode joueur vs AI (2) ou Mode AI vs AI (3) ou Mode Debug (4) : ")
    
    flag = False
    
    while(not flag):
        
        flag = True
        
        if(inputStr == "1"):
            modeJcJ = ModeJoueurContreJoueur()
            modeJcJ.commencerPartie()
        elif(inputStr == "2"):
            modeJcO = ModeJoueurContreOrdinateur()
            modeJcO.commencerPartie()
        elif(inputStr == "3"):
            modeOcO = ModeOrdinateurContreOrdinateur()
            modeOcO.commencerPartie()
        elif(inputStr == "4"):
            #tree = Utils.Rt
            Utils.createTreeFromBoard(chess.Board(), 0)
        else:
            flag = False
            inputStr = input("Mode joueur vs joueur (1) ou Mode joueur vs AI (2) ou Mode AI vs AI (3) ou Mode Debug (4) : ")
    
if __name__ == "__main__":
    main()
    main()