# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 18:40:33 2023

@author: franc

sdev 220 spring 2023
"""


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

def insert(root, value):
    if root == None:
        return Node(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
        
    return root


def inOrder(root):
    if root != None:
        inOrder(root.left)
        print("<<<---   " + str(root.value) + "    --->>>") 
        inOrder(root.right)


def preOrder(root):
    if root != None:
        print("<<<---   " + str(root.value) + "    --->>>")
        preOrder(root.left)
        preOrder(root.right)
        

def postOrder(root):
    if root != None:
        postOrder(root.left)
        postOrder(root.right)
        print("<<<---   " + str(root.value) + "    --->>>")




def search(root, key):
    print("...")
    if root == None:
        return False
    
    if root.value == key:
        return root.value
    elif key < root.value:
        return search(root.left, key)
    elif key > root.value:
        return search(root.right, key)
    






















    