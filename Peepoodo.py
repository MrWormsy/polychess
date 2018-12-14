# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 09:35:35 2018

@author: MrWormsy
"""

from ModeJoueurContreJoueur import ModeJoueurContreJoueur
from ModeJoueurContreOrdinateur import ModeJoueurContreOrdinateur

def main():
    
    inputStr = input("Mode joueur vs joueur (1) ou Mode joueur vs AI (2) ou Mode AI vs AI (3) : ")
    
    if(inputStr == "1"):
        modeJcJ = ModeJoueurContreJoueur()
        modeJcJ.commencerPartie()
    elif(inputStr == "2"):
        modeJcO = ModeJoueurContreOrdinateur()
        modeJcO.commencerPartie()
        
    
if __name__ == "__main__":
    main()  