# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:19:52 2021

@author: Personal
"""

class Node:
    def __init__(self):
        self.children={}
        self.endofword=False
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,word):
        ptr=self.root
        for letter in word:
            if letter not in ptr.children:
                ptr.children[letter]=Node()
            ptr=ptr.children[letter]
        ptr.endofword=True
        
    def search(self,word):
        ptr=self.root
        for letter in word:
            if letter not in ptr.children:
                return False
            ptr=ptr.children[letter]
        if ptr.endofword:
            return True
        else:
            return False
        
    def startswith(self,prefix):
        ptr=self.root
        for letter in prefix:
            if letter not in ptr.children:
                return False
            ptr=ptr.children[letter]
        return True
    
trie=Trie()
trie.insert("apple");
print(trie.search("apple"));
print(trie.search("app"));
print(trie.startswith("app"));
    
        