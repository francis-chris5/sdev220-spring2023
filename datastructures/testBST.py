# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:52:17 2023

@author: franc

sdev 220 spring 2023
"""

import myBST as bst


tree = bst.Node(14)
bst.insert(tree, 2)
bst.insert(tree, 29)
bst.insert(tree, 7)
bst.insert(tree, 13)
bst.insert(tree, 11)
bst.insert(tree, 21)
bst.insert(tree, 18)
bst.insert(tree, 15)
bst.insert(tree, 5)
bst.insert(tree, 1)
bst.insert(tree, 32)
bst.insert(tree, 13)
bst.insert(tree, 22)

print("\n\n**************************************\n inorder")
bst.inOrder(tree)
print("\n\n**************************************\n preorder")
bst.preOrder(tree)
print("\n\n**************************************\n postorder")
bst.postOrder(tree)

print("\n\n**************************************\n search")
if bst.search(tree, 57):
    print("found a 57")
else:
    print("57 isn't in this tree")
    
    
if bst.search(tree, 21):
    print("found a 21")
else:
    print("21 isn't in this tree")



























