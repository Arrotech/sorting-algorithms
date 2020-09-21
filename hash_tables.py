#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    # i'm going to use arrays
    # magazine edge cases
    # ensure that the magazine has atleast one word
    if len(magazine) < 1:
        return print("No")

    # ensure that the number of words to do exceed 3000
    if len(note) > 3000:
        return print("No")

    # get the index of the i
    for m_word in magazine:
        m_index = magazine.index(m_word)
        if len(magazine[m_index]) < 1:
            return print("No")
        for n_word in note:
            n_index = note.index(n_word)
            if len(note[n_index]) <= 5 and len(note[n_index]) >= 1:
                for note[n_index] in magazine:
                    for note[n_index] in note:
                        return print("Yes")
            return print("No")
            
                

            


checkMagazine(["hey","today", "night", "we", "shall", "conquer"], ["today", "night", "we", "shall", "conquer"])
