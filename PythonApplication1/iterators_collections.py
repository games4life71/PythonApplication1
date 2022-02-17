from itertools import combinations, count, permutations
import collections

class Evens(object):

    """A iterator class that generates all even numbers up to the 'limit' field """
    def __init__(self , limit) :
        self._limit = limit
        self._val = 0
    
    #Make this class iterable 
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._val <= self._limit:
            return_val = self._val
            self._val +=2
            return return_val
        else : raise StopIteration








