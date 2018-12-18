# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 09:04:54 2018

@author: anton
"""

class Node:    
    def __init__(self, content, childrens = []):
        self.content = content
        self.childrens = childrens
    
    def getContent(self):
        return self.content
    
    def getChildrens(self):
        return self.childrens
    
class RTree(Node):
    
    """
    A RTree is represented by its root Node
    """
    def __init__(self, labels, sub_RTree = []):
        super().__init__(labels, sub_RTree)

    """
    Return the root of a given RTree
    getRoot : RTree --> RTree
    """
        
    def getRoot(self):
        return self
    
    """
    Return the subTrees of a given RTree
    getRoot : RTree --> List of RTree
    """
    
    def getSubTree(self):
        return self.getChildrens()
    
    """
    Return True if the given RTree is empty
    isEmpty : RTree --> boolean
    """
    
    def isEmpty(self):
        if (self.content == None):
            return True
        else:
            return False
    
def createTreeFromBoard(board, level):
    
    if(board.is_game_over() or level >= 2):
        return
    
    level = level + 1
    
    for move in board.legal_moves:
        print(move.__str__().rjust(level * 5))
        
        #Le soucis est que on veut avoir seulement les coups des blancs alors que c'est alterné avec les blancs et les noirs, donc on fait un coups dans le vide pour faire genre que les noirs ont joué
        
        board.push(move)
        board.push(move)
        createTreeFromBoard(board, level)
        board.pop()
        board.pop()
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    