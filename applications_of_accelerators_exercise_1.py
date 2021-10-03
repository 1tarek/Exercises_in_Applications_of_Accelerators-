'''
- Create a GitHUB account.
- Write a function in Python code that adds 2+2 and returns the result.
- Write a function in Python code that multiples two 3x3 Matrices (ndarray)
  and returns the result.
- Place your code in the GitHUB repository
'''

import numpy as np


def func1():
    a=2+2
    print(a)
func1()



A=np.array([[5,6,7],[5,6,7],[5,6,7]])
B=np.array([[1,2,3],[4,5,6],[7,8,9]])

def func2():
    C=A*B
    print(C)
func2()

