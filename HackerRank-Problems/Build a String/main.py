import os
import sys

#
# Complete the buildString function below.
#


# first input is test cases 
# second input is N A B | N = length of string to be built | A = cost to add character at the end of string s | 
#                                                          | B = cost of adding substring of s at the end of string s

def buildString(a, b, s):
    #
    # Write your code here.
    #
    minCost = 0
    temp = ''
    st = list(s)
    minCost = a
    print(st)
    # ['a', 'a', 'b', 'a', 'a', 'c', 'a', 'b', 'a']
    length = 0
    i = 1
    while length != len(str):

       i += 1


    return minCost
 
# dijkstra and LCP to solve this problem 



if __name__ == '__main__':

    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    s = input("Enter string to be built: ")
    total = buildString(a,b,s)
    print(total)
